from http import HTTPStatus
from typing import Mapping

from metmuseum.responses import Response


class FakeResponse(Response):
    def __init__(
        self,
        url: str,
        status_code: HTTPStatus,
        headers: Mapping[str, str],
        data: bytes,
    ):
        self.__url = url
        self.__status_code = status_code
        self.__headers = headers
        self.__data = data

    @property
    def url(self) -> str:
        return self.__url

    @property
    def status_code(self) -> HTTPStatus:
        return self.__status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return self.__headers

    async def read(self) -> bytes:
        return self.__data


__all__ = ("FakeResponse",)
