from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any, Optional, Union

from .errors import HTTPException

if TYPE_CHECKING:
    from .http import HTTPClient, Route

__all__ = ("Ratelimiter",)

logger = logging.getLogger(__name__)


class Ratelimiter:
    """
    A class representing a Ratelimiter.

    Attributes:
        http (HTTPClient): The [HTTPClient](./http.md) instance.
        route (Route): The Route instance.
        method (str): The method to use.
        kwargs (dict): The kwargs to use.
        loop (asyncio.AbstractEventLoop): The event loop.
        global_ (asyncio.Event): The global event.
        return_data (Union[dict, str]): The return data.
        error_return (Optional[HTTPException]): The error return.

    """

    def __init__(self, http: HTTPClient, route: Route, method: str, **kwargs) -> None:
        """
        Initializes the Ratelimiter.

        Parameters:
            http (HTTPClient): The [HTTPClient](./http.md) instance.
            route (Route): The Route instance.
            method (str): The method to use.
            kwargs (dict): The kwargs to use.
        """
        self.loop: asyncio.AbstractEventLoop = http.loop
        self.global_: asyncio.Event = asyncio.Event()
        self.http: HTTPClient = http
        self.bucket: str = route.bucket
        self.route: Route = route
        self.method: str = method
        self.kwargs = kwargs

        self.return_data: Union[dict, str]
        self.error_return: Optional[HTTPException] = None
        self.global_.set()

    async def set_semaphore(self) -> asyncio.Semaphore:
        """
        Sets the semaphore for the bucket.

        Returns:
            The asyncio.Semaphore for the bucket.
        """
        if semaphore := self.http.semaphores.get(self.bucket):
            return semaphore

        resp = await self.http.session.request(
            "HEAD",
            self.route.url,
            headers={"Authorization": f"Bot {self.http.token}"},
        )
        semaphore = asyncio.Semaphore(int(resp.headers.get("X-Ratelimit-Limit", 1)))
        self.http.semaphores[self.bucket] = semaphore

        return semaphore

    async def release(self, semaphore: asyncio.Semaphore, delay: float) -> None:
        """
        Releases the semaphore after a delay.

        Parameters:
            semaphore: The semaphore to release.
            delay: The delay after which semaphore is to be released.
        """
        await asyncio.sleep(delay)
        semaphore.release()

    def global_ratelimit_set(self, delay: float) -> None:
        """
        Sets the global ratelimit.

        Parameters:
            delay: The delay to set for the global ratelimit.
        """
        self.loop.call_later(delay, self.global_.set)

    async def request(self) -> Any:
        """
        Makes a request to the route.

        Returns:
            The response from the route.
        """
        semaphore = self.http.semaphores.get(self.bucket, await self.set_semaphore())
        session = self.http.session

        await asyncio.gather(
            self.global_.wait(), semaphore.acquire(), self.route.lock.acquire()
        )
        resp = await session.request(self.method, self.route.url, **self.kwargs)
        data = await self.http.json_or_text(resp)

        reset_after: float = float(resp.headers.get("X-Ratelimit-Reset-After", 0))
        remaining: int = int(resp.headers.get("X-Ratelimit-Remaining", 1))

        if resp.status != 429 and remaining == 0:
            logger.info(f"BUCKET DEPLETED: {self.bucket} RETRY: {reset_after}s")
            self.loop.call_later(reset_after, self.route.lock.release)
            await self.release(semaphore, reset_after)
            await self.request()

        if 300 > resp.status >= 200:
            logger.info(
                f"{resp.status}: {self.method} ROUTE: {self.route.url} REMAINING: {remaining}"
            )
            return data

        if resp.status == 429:
            retry_after: float = data["retry_after"]  # type: ignore
            logger.info(
                f"RATELIMITED: {self.method} ROUTE: {self.route.url} RETRY: {retry_after}"
            )
            if data.get("global", False):  # type: ignore
                self.global_.clear()

            self.global_ratelimit_set(retry_after)
            await asyncio.sleep(retry_after)
            await self.request()

        if not 300 > resp.status >= 200:
            logger.info(
                f"FAILED: {self.method} : ROUTE: {self.route.url} STATUS: {resp.status}"
            )
            raise self.http.ERRORS.get(resp.status, HTTPException)(data)

    async def __aenter__(self) -> Ratelimiter:
        return self

    async def __aexit__(self, *_) -> None:
        self.http.semaphores.pop(self.bucket)
