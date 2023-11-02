from typing import Mapping, Any
from abc import ABC, abstractmethod

import aiohttp


class Client(ABC):
    @abstractmethod
    async def request(
            self,
            url: str,
            method: str,
            data: Any | None,
            json: dict | str | None,
            params: Mapping[str, str] | None
    ):
        pass


class AIOClient(Client):
    async def request(
            self,
            url: str,
            method: str,
            data: Any | None,
            json: dict | str | None,
            params: Mapping[str, str] | None
    ):
        async with aiohttp.ClientSession() as session:
            return await session.request(
                url=url,
                method=method,
                data=data,
                json=json,
                params=params
            )


aio_client = AIOClient()
