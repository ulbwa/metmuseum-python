from abc import abstractmethod
from http import HTTPStatus
from typing import Mapping, Protocol


class Response(Protocol):
    @property
    @abstractmethod
    def url(self) -> str: ...

    @property
    @abstractmethod
    def status_code(self) -> HTTPStatus: ...

    @property
    @abstractmethod
    def headers(self) -> Mapping[str, str]: ...

    @property
    @abstractmethod
    def ok(self) -> bool: ...

    @abstractmethod
    async def read(self) -> bytes: ...


__all__ = ("Response",)
