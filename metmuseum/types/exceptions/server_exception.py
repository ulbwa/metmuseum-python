from http import HTTPStatus
from typing import Mapping

from metmuseum.types.exceptions.api_exception import ApiException


class ServerException(ApiException):
    def __init__(self, status_code: HTTPStatus, headers: Mapping[str, str], data: bytes):
        assert 500 <= status_code <= 599

        super().__init__(status_code, headers, data)


__all__ = ("ServerException",)
