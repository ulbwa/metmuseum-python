from datetime import date
from http import HTTPMethod, HTTPStatus

import pytest
from pydantic import ValidationError

from metmuseum.metmuseum import MetMuseum
from metmuseum.types import responses
from tests.mocks import FakeGateway, FakeResponse


@pytest.fixture
def fake_gateway_with_empty_data() -> FakeGateway:
    fake_response = FakeResponse(
        url="https://fake.url/objects",
        status_code=HTTPStatus.OK,
        headers={},
        data=b"",
    )
    return FakeGateway(fake_response)


@pytest.fixture
def fake_gateway_with_objects_example() -> FakeGateway:
    fake_data = b"""{
	"total": 471581,
	"objectIDs": [
		1,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9,
		10
	]
}"""
    fake_response = FakeResponse(
        url="https://fake.url/objects",
        status_code=HTTPStatus.OK,
        headers={},
        data=fake_data,
    )
    return FakeGateway(fake_response)


async def test_objects_with_objects_example(
    fake_gateway_with_objects_example: FakeGateway,
):
    base_url = "https://fake.url"
    metmuseum = MetMuseum(gateway=fake_gateway_with_objects_example, base_url=base_url)
    objects_response = await metmuseum.list_objects()

    assert fake_gateway_with_objects_example.method == HTTPMethod.GET
    assert fake_gateway_with_objects_example.url == "https://fake.url/objects"
    assert fake_gateway_with_objects_example.data is None
    assert fake_gateway_with_objects_example.headers is None
    assert fake_gateway_with_objects_example.query is None

    assert isinstance(objects_response, responses.ObjectsResponse)

    assert objects_response.total == 471581
    assert objects_response.ids == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


async def test_objects_with_objects_example_with_query_params(
    fake_gateway_with_objects_example: FakeGateway,
):
    base_url = "https://fake.url"
    metmuseum = MetMuseum(gateway=fake_gateway_with_objects_example, base_url=base_url)
    metadata_date = date(2020, 1, 1)
    department_ids = (1, 2, 3, 4, 5)
    objects_response = await metmuseum.list_objects(
        metadata_date=metadata_date, department_ids=department_ids
    )

    assert fake_gateway_with_objects_example.method == HTTPMethod.GET
    assert fake_gateway_with_objects_example.url == "https://fake.url/objects"
    assert fake_gateway_with_objects_example.data is None
    assert fake_gateway_with_objects_example.headers is None
    assert fake_gateway_with_objects_example.query is not None
    assert fake_gateway_with_objects_example.query["metadataDate"] == "2020-01-01"
    assert fake_gateway_with_objects_example.query["departmentIds"] == "1|2|3|4|5"

    assert isinstance(objects_response, responses.ObjectsResponse)

    assert objects_response.total == 471581
    assert objects_response.ids == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


async def test_objects_with_empty_data(fake_gateway_with_empty_data: FakeGateway):
    base_url = "https://fake.url"
    metmuseum = MetMuseum(gateway=fake_gateway_with_empty_data, base_url=base_url)

    with pytest.raises(ValidationError):
        await metmuseum.list_objects()


@pytest.fixture
def fake_gateway_with_object_example() -> FakeGateway:
    fake_data = """{
    "objectID": 45734,
    "isHighlight": false,
    "accessionNumber": "36.100.45",
    "accessionYear": "1936",
    "isPublicDomain": true,
    "primaryImage": "https://images.metmuseum.org/CRDImages/as/original/DP251139.jpg",
    "primaryImageSmall": "https://images.metmuseum.org/CRDImages/as/web-large/DP251139.jpg",
    "additionalImages": [
        "https://images.metmuseum.org/CRDImages/as/original/DP251138.jpg",
        "https://images.metmuseum.org/CRDImages/as/original/DP251120.jpg"
    ],
    "constituents": [
        {
            "constituentID": 11986,
            "role": "Artist",
            "name": "Kiyohara Yukinobu",
            "constituentULAN_URL": "http://vocab.getty.edu/page/ulan/500034433",
            "constituentWikidata_URL": "https://www.wikidata.org/wiki/Q11560527",
            "gender": "Female"
        }
    ],
    "department": "Asian Art",
    "objectName": "Hanging scroll",
    "title": "Quail and Millet",
    "culture": "Japan",
    "period": "Edo period (1615–1868)",
    "dynasty": "",
    "reign": "",
    "portfolio": "",
    "artistRole": "Artist",
    "artistPrefix": "",
    "artistDisplayName": "Kiyohara Yukinobu",
    "artistDisplayBio": "Japanese, 1643–1682",
    "artistSuffix": "",
    "artistAlphaSort": "Kiyohara Yukinobu",
    "artistNationality": "Japanese",
    "artistBeginDate": "1643",
    "artistEndDate": "1682",
    "artistGender": "Female",
    "artistWikidata_URL": "https://www.wikidata.org/wiki/Q11560527",
    "artistULAN_URL": "http://vocab.getty.edu/page/ulan/500034433",
    "objectDate": "late 17th century",
    "objectBeginDate": 1667,
    "objectEndDate": 1682,
    "medium": "Hanging scroll; ink and color on silk",
    "dimensions": "46 5/8 x 18 3/4 in. (118.4 x 47.6 cm)",
    "measurements": [
        {
            "elementName": "Overall",
            "elementDescription": null,
            "elementMeasurements": {
                "Height": 118.4,
                "Width": 47.6
            }
        }
    ],
    "creditLine": "The Howard Mansfield Collection, Purchase, Rogers Fund, 1936",
    "geographyType": "",
    "city": "",
    "state": "",
    "county": "",
    "country": "",
    "region": "",
    "subregion": "",
    "locale": "",
    "locus": "",
    "excavation": "",
    "river": "",
    "classification": "Paintings",
    "rightsAndReproduction": "",
    "linkResource": "",
    "metadataDate": "2020-09-14T12:26:37.48Z",
    "repository": "Metropolitan Museum of Art, New York, NY",
    "objectURL": "https://www.metmuseum.org/art/collection/search/45734",
    "tags": [
        {
            "term": "Birds",
            "AAT_URL": "http://vocab.getty.edu/page/aat/300266506",
            "Wikidata_URL": "https://www.wikidata.org/wiki/Q5113"
        }
    ],
    "objectWikidata_URL": "https://www.wikidata.org/wiki/Q29910832",
    "isTimelineWork": false,
    "GalleryNumber": ""
}""".encode()
    fake_response = FakeResponse(
        url="https://youtu.be/dQw4w9WgXcQ",
        status_code=HTTPStatus.OK,
        headers={},
        data=fake_data,
    )
    return FakeGateway(fake_response)


async def test_object_with_object_example(
    fake_gateway_with_object_example: FakeGateway,
):
    base_url = "https://fake.url"
    metmuseum = MetMuseum(gateway=fake_gateway_with_object_example, base_url=base_url)
    object_response = await metmuseum.get_object(45734)

    assert fake_gateway_with_object_example.method == HTTPMethod.GET
    assert fake_gateway_with_object_example.url == "https://fake.url/objects/45734"
    assert fake_gateway_with_object_example.data is None
    assert fake_gateway_with_object_example.headers is None
    assert fake_gateway_with_object_example.query is None

    assert isinstance(object_response, responses.ObjectResponse)

    # i think we should be able to validate the object response,
    # but the data is so large that it's not worth it, pydantic already handled it


async def test_object_with_empty_data(fake_gateway_with_empty_data: FakeGateway):
    base_url = "https://fake.url"
    metmuseum = MetMuseum(gateway=fake_gateway_with_empty_data, base_url=base_url)

    with pytest.raises(ValidationError):
        await metmuseum.get_object(45734)


@pytest.fixture
def fake_gateway_with_departments_example() -> FakeGateway:
    fake_data = b"""{
  "departments": [
    {
      "departmentId": 1,
      "displayName": "American Decorative Arts"
    },
    {
      "departmentId": 3,
      "displayName": "Ancient Near Eastern Art"
    },
    {
      "departmentId": 4,
      "displayName": "Arms and Armor"
    },
    {
      "departmentId": 5,
      "displayName": "Arts of Africa, Oceania, and the Americas"
    },
    {
      "departmentId": 6,
      "displayName": "Asian Art"
    },
    {
      "departmentId": 7,
      "displayName": "The Cloisters"
    },
    {
      "departmentId": 8,
      "displayName": "The Costume Institute"
    },
    {
      "departmentId": 9,
      "displayName": "Drawings and Prints"
    },
    {
      "departmentId": 10,
      "displayName": "Egyptian Art"
    },
    {
      "departmentId": 11,
      "displayName": "European Paintings"
    },
    {
      "departmentId": 12,
      "displayName": "European Sculpture and Decorative Arts"
    },
    {
      "departmentId": 13,
      "displayName": "Greek and Roman Art"
    },
    {
      "departmentId": 14,
      "displayName": "Islamic Art"
    },
    {
      "departmentId": 15,
      "displayName": "The Robert Lehman Collection"
    },
    {
      "departmentId": 16,
      "displayName": "The Libraries"
    },
    {
      "departmentId": 17,
      "displayName": "Medieval Art"
    },
    {
      "departmentId": 18,
      "displayName": "Musical Instruments"
    },
    {
      "departmentId": 19,
      "displayName": "Photographs"
    },
    {
      "departmentId": 21,
      "displayName": "Modern Art"
    }
  ]
}"""
    fake_response = FakeResponse(
        url="https://fake.url/departments",
        status_code=HTTPStatus.OK,
        headers={},
        data=fake_data,
    )
    return FakeGateway(fake_response)


async def test_departments_with_departments_example(
    fake_gateway_with_departments_example: FakeGateway,
):
    metmuseum = MetMuseum(
        gateway=fake_gateway_with_departments_example, base_url="https://fake.url"
    )
    departments_response = await metmuseum.list_departments()

    assert fake_gateway_with_departments_example.method == HTTPMethod.GET
    assert fake_gateway_with_departments_example.url == "https://fake.url/departments"
    assert fake_gateway_with_departments_example.data is None
    assert fake_gateway_with_departments_example.headers is None
    assert fake_gateway_with_departments_example.query is None

    assert isinstance(departments_response, responses.DepartmentsResponse)
    assert isinstance(departments_response.departments, tuple)
    assert len(departments_response.departments) == 19
    assert departments_response.departments[0].id == 1
    assert departments_response.departments[0].display_name == "American Decorative Arts"


async def test_departments_with_empty_data(fake_gateway_with_empty_data: FakeGateway):
    metmuseum = MetMuseum(
        gateway=fake_gateway_with_empty_data, base_url="https://fake.url"
    )

    with pytest.raises(ValidationError):
        await metmuseum.list_departments()


@pytest.fixture
def fake_gateway_with_search_example() -> FakeGateway:
    fake_data = b"""{
	"total": 27,
	"objectIDs": [
		1,
		2,
		3
	]
}"""
    fake_response = FakeResponse(
        url="https://fake.url/search",
        status_code=HTTPStatus.OK,
        headers={},
        data=fake_data,
    )
    return FakeGateway(fake_response)


async def test_search_with_search_example_with_query_params(
    fake_gateway_with_search_example: FakeGateway,
):
    metmuseum = MetMuseum(
        gateway=fake_gateway_with_search_example, base_url="https://fake.url"
    )
    search_response = await metmuseum.search(
        query="Some query",
        is_highlight=True,
        title=True,
        tags=False,
        department_id=4,
        is_on_view=None,
        artist_or_culture=None,
        medium=["First", "Second"],
        has_images=True,
        geo_location=None,
        date_begin=1,
        date_end=5,
    )

    assert fake_gateway_with_search_example.method == HTTPMethod.GET
    assert fake_gateway_with_search_example.url == "https://fake.url/search"
    assert fake_gateway_with_search_example.data is None
    assert fake_gateway_with_search_example.headers is None
    assert fake_gateway_with_search_example.query is not None
    assert fake_gateway_with_search_example.query["q"] == "Some query"
    assert fake_gateway_with_search_example.query["isHighlight"] == "true"
    assert fake_gateway_with_search_example.query["title"] == "true"
    assert fake_gateway_with_search_example.query["tags"] == "false"
    assert fake_gateway_with_search_example.query["departmentId"] == "4"
    assert "isOnView" not in fake_gateway_with_search_example.query
    assert "artistOrCulture" not in fake_gateway_with_search_example.query
    assert fake_gateway_with_search_example.query["medium"] == "First|Second"
    assert fake_gateway_with_search_example.query["hasImages"] == "true"
    assert "geoLocation" not in fake_gateway_with_search_example.query
    assert fake_gateway_with_search_example.query["dateBegin"] == "1"
    assert fake_gateway_with_search_example.query["dateEnd"] == "5"

    assert isinstance(search_response, responses.SearchResponse)

    assert search_response.total == 27
    assert search_response.ids == (1, 2, 3)


async def test_search_with_search_example_with_invalid_query_params(
    fake_gateway_with_search_example: FakeGateway,
):
    metmuseum = MetMuseum(
        gateway=fake_gateway_with_search_example, base_url="https://fake.url"
    )

    with pytest.raises(ValueError):
        await metmuseum.search(query="valid query", date_begin=1)
