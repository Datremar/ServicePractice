from typing import Any, Mapping

from core.client.clients import Client, aio_client
from core.client.requests.request import Request
from core.client.urls import DATABASE_URL


class DatabaseRequest(Request):
    def __init__(self, client: Client):
        self.url = DATABASE_URL
        self.client = client

    async def get(self, endpoint: str):
        return await self.client.request(
            url=self.url + endpoint,
            method="GET",
            data=None,
            json=None,
            params=None
        )

    async def post(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        return await self.client.request(
            url=self.url + endpoint,
            method="POST",
            data=data,
            json=json,
            params=params
        )

    async def put(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        return await self.client.request(
            url=self.url + endpoint,
            method="PUT",
            data=data,
            json=json,
            params=params
        )

    async def delete(
            self,
            endpoint: str,
            data: Any | None,
            json: str | dict | None,
            params: Mapping[str, str] | None
    ):
        return await self.client.request(
            url=self.url + endpoint,
            method="DELETE",
            data=data,
            json=json,
            params=params
        )


database_request = DatabaseRequest(client=aio_client)
