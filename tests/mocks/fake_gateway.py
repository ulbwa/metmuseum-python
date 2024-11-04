from contextlib import asynccontextmanager
from http import HTTPMethod
from typing import AsyncIterator, Mapping

from metmuseum.gateways import HttpGateway
from metmuseum.responses import Response


class FakeGateway(HttpGateway):
    def __init__(self, response: Response):
        self.__response = response

    @asynccontextmanager
    async def make_request(
        self,
        method: HTTPMethod,
        url: str,
        query: Mapping[str, str] | None = None,
        headers: Mapping[str, str] | None = None,
        data: bytes | None = None,
    ) -> AsyncIterator[Response]:
        self.method = method
        self.url = url
        self.query = query
        self.headers = headers
        self.data = data
        yield self.__response


__all__ = ("FakeGateway",)
