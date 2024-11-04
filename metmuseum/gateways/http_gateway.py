from http import HTTPMethod
from typing import AsyncContextManager, Mapping, Protocol

from metmuseum.responses.response import Response


class HttpGateway(Protocol):
    def make_request(
        self,
        method: HTTPMethod,
        url: str,
        query: Mapping[str, str] | None = None,
        headers: Mapping[str, str] | None = None,
        body: bytes | None = None,
    ) -> AsyncContextManager[Response]: ...


__all__ = ("HttpGateway",)
