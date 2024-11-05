import json
from functools import cached_property
from http import HTTPStatus
from typing import Mapping


class ApiException(Exception):
    __slots__ = "__status_code", "__headers", "__data"

    def __init__(self, status_code: HTTPStatus, headers: Mapping[str, str], data: bytes):
        assert 400 <= status_code <= 599

        self.__status_code = status_code
        self.__headers = headers
        self.__data = data

        super(Exception, self).__init__(self.detail)

    @property
    def status_code(self) -> HTTPStatus:
        return self.__status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return self.__headers

    @property
    def data(self) -> bytes:
        return self.__data

    @cached_property
    def detail(self) -> str:
        content_type = self.headers.get("Content-Type")
        if content_type is not None:
            content_type_parsed = content_type.split("; ")

            if "text/plain" in content_type_parsed:
                text = self.data.decode("utf-8")
                return f"{self.status_code.phrase}: {text}"

            elif "application/json" in content_type_parsed:
                text = json.loads(self.data.decode("utf-8"))
                if isinstance(text, str):
                    return f"{self.status_code.phrase}: {text}"

        if self.status_code.description:
            return f"{self.status_code.phrase}: {self.status_code.description}"
        else:
            return self.status_code.phrase


__all__ = ("ApiException",)
