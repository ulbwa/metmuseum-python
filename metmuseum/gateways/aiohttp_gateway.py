from contextlib import asynccontextmanager
from http import HTTPMethod
from logging import getLogger
from typing import AsyncIterator, Mapping
from uuid import uuid4

from aiohttp import ClientSession

from metmuseum.adapters import AiohttpResponseAdapter
from metmuseum.gateways.http_gateway import HttpGateway
from metmuseum.responses import Response


class AiohttpGateway(HttpGateway):
    __slots__ = ("__logger",)

    def __init__(self):
        self.__logger = getLogger("metmuseum:aiohttp-gateway")

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[ClientSession]:
        async with ClientSession() as session:
            yield session

    @asynccontextmanager
    async def make_request(
        self,
        method: HTTPMethod,
        url: str,
        query: Mapping[str, str] | None = None,
        headers: Mapping[str, str] | None = None,
        body: bytes | None = None,
    ) -> AsyncIterator[Response]:
        async with self.get_session() as session:
            req_id = uuid4()
            self.__logger.debug(f"Request: {req_id} {method.value} {url}")

            async with session.request(
                method.value, url, params=query, data=body, headers=headers
            ) as raw_response:
                response = AiohttpResponseAdapter(raw_response)
                self.__logger.debug(f"Response: {req_id} {response.status_code}")

                yield response


__all__ = ("AiohttpGateway",)
