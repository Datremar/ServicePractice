from abc import ABC, abstractmethod
from typing import Any, Mapping

from core.client.clients import Client


class Request(ABC):
    @abstractmethod
    def __init__(self, url: str, client: Client):
        pass

    @abstractmethod
    async def get(self, endpoint: str):
        pass

    @abstractmethod
    async def post(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        pass

    @abstractmethod
    async def put(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        pass

    @abstractmethod
    async def delete(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        pass
