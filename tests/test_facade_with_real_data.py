from datetime import date, datetime, timedelta
from http import HTTPStatus
from os import getenv

import pytest

from metmuseum.gateways.aiohttp_gateway import AiohttpGateway
from metmuseum.metmuseum import MetMuseum
from metmuseum.types import responses
from metmuseum.types.exceptions.client_exception import ClientException
from metmuseum.types.exceptions.server_exception import ServerException


@pytest.fixture
def metmuseum_url() -> str:
    return getenv(
        "METMUSEUM_URL", "https://collectionapi.metmuseum.org/public/collection/v1"
    )


@pytest.fixture
def metmuseum(metmuseum_url: str) -> MetMuseum:
    gateway = AiohttpGateway()
    return MetMuseum(gateway=gateway, base_url=metmuseum_url)


async def test_objects(metmuseum: MetMuseum):
    objects_response = await metmuseum.list_objects()
    assert isinstance(objects_response, responses.ObjectsResponse)
    assert len(objects_response.ids) == objects_response.total


async def test_objects_with_query_params(metmuseum: MetMuseum):
    objects_response = await metmuseum.list_objects(
        metadata_date=date(2024, 1, 1), department_ids=(1, 2)
    )
    assert isinstance(objects_response, responses.ObjectsResponse)


async def test_objects_with_future_metadata_date(metmuseum: MetMuseum):
    objects_response = await metmuseum.list_objects(
        metadata_date=(datetime.now() + timedelta(days=7)).date()
    )
    assert isinstance(objects_response, responses.ObjectsResponse)
    assert objects_response.total == 0
    assert len(objects_response.ids) == objects_response.total


async def test_objects_with_empty_departments(metmuseum: MetMuseum):
    objects_response = await metmuseum.list_objects(department_ids=())
    assert isinstance(objects_response, responses.ObjectsResponse)
    assert objects_response.total > 0
    assert len(objects_response.ids) == objects_response.total


async def test_objects_with_negative_departments(metmuseum: MetMuseum):
    objects_response = await metmuseum.list_objects(department_ids=(-1000,))
    assert isinstance(objects_response, responses.ObjectsResponse)
    assert objects_response.total == 0
    assert len(objects_response.ids) == objects_response.total


async def test_objects_with_invalid_departments(metmuseum: MetMuseum):
    # a 400 error is expected, but a 500 error is returned,
    # this api behavior needs to be fixed
    with pytest.raises(ServerException) as exception:
        await metmuseum.list_objects(department_ids=("invalid",))  # type: ignore

    assert exception.value.status_code == HTTPStatus.BAD_GATEWAY


async def test_object(metmuseum: MetMuseum):
    object_response = await metmuseum.get_object(10)
    assert isinstance(object_response, responses.ObjectResponse)


async def test_object_not_found(metmuseum: MetMuseum):
    with pytest.raises(ClientException) as exception:
        await metmuseum.get_object(1233)

    assert exception.value.status_code == HTTPStatus.NOT_FOUND


async def test_object_with_invalid_id(metmuseum: MetMuseum):
    with pytest.raises(ClientException) as exception:
        await metmuseum.get_object("invalid")  # type: ignore

    assert exception.value.status_code == HTTPStatus.BAD_REQUEST


async def test_search(metmuseum: MetMuseum):
    search_response = await metmuseum.search(query="rapper")
    assert isinstance(search_response, responses.SearchResponse)
    assert search_response.total >= 1
    assert search_response.ids is not None
    assert len(search_response.ids) == search_response.total


async def test_search_not_found(metmuseum: MetMuseum):
    search_response = await metmuseum.search(query="X" * 100)
    assert isinstance(search_response, responses.SearchResponse)
    assert search_response.total == 0
    assert search_response.ids is None


async def test_search_with_query_params(metmuseum: MetMuseum):
    search_response = await metmuseum.search(
        query="Laurence Augustine",
        medium=["Canvas"],
        geo_location=["France"],
        date_begin=1800,
        date_end=1900,
    )
    assert isinstance(search_response, responses.SearchResponse)
    assert search_response.total == 1
    assert search_response.ids is not None
    assert len(search_response.ids) == search_response.total


async def test_departments(metmuseum: MetMuseum):
    departments_response = await metmuseum.list_departments()
    assert isinstance(departments_response, responses.DepartmentsResponse)
