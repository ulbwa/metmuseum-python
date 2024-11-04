import json
from http import HTTPMethod, HTTPStatus
from os import getenv

import pytest

from metmuseum.gateways import AiohttpGateway


@pytest.fixture
def httpbin_url() -> str:
    return getenv("HTTPBIN_URL", "https://httpbin.org")


@pytest.fixture
async def aiohttp_gateway() -> AiohttpGateway:
    a = AiohttpGateway()
    return a


async def test_httpbin_get_request(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.GET,
        httpbin_url + "/get",
        query={"myQueryParam": "1"},
        headers={"x-my-extra-header": "my extra value"},
    ) as response:
        assert response.status_code == HTTPStatus.OK
        assert response.url == "https://httpbin.org/get?myQueryParam=1"

        data = await response.read()
        parsed_data = json.loads(data.decode("utf-8"))

        assert parsed_data["url"] == "https://httpbin.org/get?myQueryParam=1"
        assert parsed_data["headers"]["X-My-Extra-Header"] == "my extra value"
        assert parsed_data["args"]["myQueryParam"] == "1"


async def test_httpbin_post_request(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.POST,
        httpbin_url + "/post",
        query={"myQueryParam": "1"},
        headers={"x-my-extra-header": "my extra value"},
        data=b"my data",
    ) as response:
        assert response.status_code == HTTPStatus.OK
        assert response.url == "https://httpbin.org/post?myQueryParam=1"

        data = await response.read()
        parsed_data = json.loads(data.decode("utf-8"))

        assert parsed_data["url"] == "https://httpbin.org/post?myQueryParam=1"
        assert parsed_data["headers"]["X-My-Extra-Header"] == "my extra value"
        assert parsed_data["data"] == "my data"


async def test_httpbin_delete_request(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.DELETE,
        httpbin_url + "/delete",
        query={"myQueryParam": "1"},
        headers={"x-my-extra-header": "my extra value"},
        data=b"my data",
    ) as response:
        assert response.status_code == HTTPStatus.OK
        assert response.url == httpbin_url + "/delete?myQueryParam=1"

        data = await response.read()
        parsed_data = json.loads(data.decode("utf-8"))

        assert parsed_data["url"] == httpbin_url + "/delete?myQueryParam=1"
        assert parsed_data["headers"]["X-My-Extra-Header"] == "my extra value"
        assert parsed_data["data"] == "my data"


async def test_httpbin_patch_request(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.PATCH,
        httpbin_url + "/patch",
        query={"myQueryParam": "1"},
        headers={"x-my-extra-header": "my extra value"},
        data=b"my data",
    ) as response:
        assert response.status_code == HTTPStatus.OK
        assert response.url == httpbin_url + "/patch?myQueryParam=1"

        data = await response.read()
        parsed_data = json.loads(data.decode("utf-8"))

        assert parsed_data["url"] == httpbin_url + "/patch?myQueryParam=1"
        assert parsed_data["headers"]["X-My-Extra-Header"] == "my extra value"
        assert parsed_data["data"] == "my data"


async def test_httpbin_put_request(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.PUT,
        httpbin_url + "/put",
        query={"myQueryParam": "1"},
        headers={"x-my-extra-header": "my extra value"},
        data=b"my data",
    ) as response:
        assert response.status_code == HTTPStatus.OK
        assert response.url == httpbin_url + "/put?myQueryParam=1"

        data = await response.read()
        parsed_data = json.loads(data.decode("utf-8"))

        assert parsed_data["url"] == httpbin_url + "/put?myQueryParam=1"
        assert parsed_data["headers"]["X-My-Extra-Header"] == "my extra value"
        assert parsed_data["data"] == "my data"


async def test_httpbin_status_code(httpbin_url: str, aiohttp_gateway: AiohttpGateway):
    async with aiohttp_gateway.make_request(
        HTTPMethod.GET,
        httpbin_url + "/status/500",
    ) as response:
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
