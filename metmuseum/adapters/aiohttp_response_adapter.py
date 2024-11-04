from http import HTTPStatus
from typing import Mapping

from aiohttp import ClientResponse

from metmuseum.responses.response import Response


class AiohttpResponseAdapter(Response):
    __slots__ = ("__response",)

    def __init__(self, raw_response: ClientResponse):
        self.__response = raw_response

    @property
    def raw_response(self) -> ClientResponse:
        return self.__response

    @property
    def url(self) -> str:
        return str(self.raw_response.real_url)

    @property
    def status_code(self) -> HTTPStatus:
        return HTTPStatus(self.raw_response.status)

    @property
    def headers(self) -> Mapping[str, str]:
        return self.raw_response.headers

    async def read(self) -> bytes:
        return await self.raw_response.read()


__all__ = ("AiohttpResponseAdapter",)
