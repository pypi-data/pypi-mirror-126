from __future__ import annotations

import asyncio
import datetime
import logging
import sys
from typing import TYPE_CHECKING, Callable, Dict, List, Optional

import aiohttp

from ..objects import Intents
from .opcodes import OpCodes
from .ratelimiter import Ratelimiter

if TYPE_CHECKING:
    from ..client import Client

__all__ = ("BaseWebsocketClient",)

logger = logging.getLogger(__name__)


class BaseWebsocketClient:
    def __init__(
        self,
        client: Client,
        intents: Optional[Intents] = None,
        shard_ids: Optional[List[int]] = None,
    ) -> None:
        self.intents: Intents = Intents.default() if intents is None else intents
        self.websocket: aiohttp.ClientWebSocketResponse = None  # type: ignore
        self.client: Client = client
        self.closed: bool = False
        self.seq: int = 0

        self.last_heartbeat: Optional[datetime.datetime] = None
        self.latency: float = float("inf")
        self.heartbeat_delay: float = 0

    async def _get_gateway(self) -> Dict:
        headers = {"Authorization": f"Bot {self.client.http.token}"}
        session = self.client.http.session or await self.client.http._create_session()

        resp = await session.request(
            "GET", "https://discord.com/api/v9/gateway/bot", headers=headers
        )
        return await resp.json()

    async def start(self) -> None:
        """
        Starts the connection to the websocket and begins parsing messages from the gateway.
        """
        data = await self._get_gateway()
        max_concurrency: int = data["session_start_limit"]["max_concurrency"]

        async with Ratelimiter(max_concurrency, 1) as handler:
            self.websocket = await self.client.http.ws_connect(data["url"])

            await self.identify()
            asyncio.gather(self.start_heartbeat(), self.read_messages())

            handler.release()

    async def read_messages(self) -> None:
        """
        Reads the messages from received from the websocket and parses them.
        """
        async for message in self.websocket:
            if message.type is aiohttp.WSMsgType.TEXT:
                recieved_data = message.json()

                if recieved_data["op"] == OpCodes.DISPATCH:
                    await self.dispatch(recieved_data["t"], recieved_data["d"])

                if recieved_data["op"] == OpCodes.HEARTBEAT_ACK:
                    if self.last_heartbeat is not None:
                        self.latency = (
                            datetime.datetime.now() - self.last_heartbeat
                        ).total_seconds() * 1000

                    logger.info("HEARTBEAT ACKNOWLEDGED")

                if recieved_data["op"] == OpCodes.RESUME:
                    logger.info("RESUMED")
                    await self.resume()

                if recieved_data["op"] == OpCodes.RECONNECT:
                    logger.info("RECONNECT")
                    await self.reconnect()

        await self.websocket.close()
        logger.info("WEBSOCKET CLOSED")

    async def dispatch(self, event: str, data: Dict) -> None:
        """
        Dispatches an event and its data to the parsers.

        Parameters:
            event (str): The event being dispatched.
            data (Dict): The raw data of the event.
        """
        logger.info(f"DISPATCHED EVENT: {event}")
        if event == "READY":
            self.session_id = data["session_id"]

        if parser := getattr(self.client._state, f"parse_{event.lower()}", None):
            return await parser(data)

        self.client._state.dispatch("websocket_message", event, data)

    async def reconnect(self) -> None:
        """
        Closes the websocket if it isn't then tries to establish a new connection.
        """
        if not self.websocket and self.websocket.closed:
            await self.websocket.close()
            self.closed = True

        await self.start()

    async def resume(self) -> None:
        """;eval return 2+2
        Sends a resume payload to the websocket.
        """
        payload = {
            "op": OpCodes.RESUME,
            "token": self.client.http.token,
            "session_id": self.session_id,
            "seq": self.seq,
        }
        await self.websocket.send_json(payload)

    async def identify(self) -> None:
        """
        Sends an identify payload to the websocket.
        """
        data = await self.websocket.receive()
        self.heartbeat_delay = data.json()["d"]["heartbeat_interval"]

        payload = {
            "op": OpCodes.IDENTIFY,
            "d": {
                "token": self.client.http.token,
                "intents": self.intents.value,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "Lefi",
                    "$device": "Lefi",
                },
            },
        }
        await self.websocket.send_json(payload)

    async def start_heartbeat(self) -> None:
        """
        Starts the heartbeat loop.
        Info:
            This can be blocked, which causes the heartbeat to stop.
        """
        while self.websocket and not self.websocket.closed:
            self.seq += 1

            await self.websocket.send_json({"op": OpCodes.HEARTBEAT, "d": self.seq})
            self.last_heartbeat = datetime.datetime.now()
            logger.info("HEARTBEAT SENT")

            await asyncio.sleep(self.heartbeat_delay / 1000)
