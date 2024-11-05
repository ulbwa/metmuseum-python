from http import HTTPStatus
from typing import Mapping

from metmuseum.types.exceptions.api_exception import ApiException


class ClientException(ApiException):
    def __init__(self, status_code: HTTPStatus, headers: Mapping[str, str], data: bytes):
        assert 400 <= status_code <= 499

        super().__init__(status_code, headers, data)


__all__ = ("ClientException",)
