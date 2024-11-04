from datetime import date
from http import HTTPMethod
from typing import Sequence, TypeVar

from metmuseum.gateways.http_gateway import HttpGateway
from metmuseum.types import exceptions, responses

AnyResponseT = TypeVar(
    "AnyResponseT",
    bound=responses.ObjectsResponse
    | responses.ObjectResponse
    | responses.SearchResponse
    | responses.DepartmentsResponse,
)


class MetMuseum:
    __slots__ = "gateway", "base_url"

    def __init__(
        self,
        gateway: HttpGateway,
        base_url: str = "https://collectionapi.metmuseum.org/public/collection/v1",
    ):
        self.gateway = gateway
        self.base_url = base_url.rstrip("/")

    async def __make_request(
        self,
        method: HTTPMethod,
        path: str,
        resp: type[AnyResponseT],
        query: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        data: bytes | None = None,
    ) -> AnyResponseT:
        async with self.gateway.make_request(
            method=method,
            url=self.base_url + path,
            query=query,
            headers=headers,
            data=data,
        ) as response:
            data = await response.read()
            if 400 <= response.status_code <= 499:
                raise exceptions.ClientException(
                    status_code=response.status_code, headers=response.headers, data=data
                )
            if 500 <= response.status_code <= 599:
                raise exceptions.ServerException(
                    status_code=response.status_code, headers=response.headers, data=data
                )
            return resp.model_validate_json(data)

    async def list_objects(
        self,
        metadata_date: date | None = None,
        department_ids: Sequence[int] | None = None,
    ) -> responses.ObjectsResponse:
        query: dict[str, str] = dict()
        if metadata_date is not None:
            query["metadataDate"] = metadata_date.strftime("%Y-%m-%d")
        if department_ids is not None:
            query["departmentIds"] = "|".join(map(str, department_ids))
        return await self.__make_request(
            method=HTTPMethod.GET,
            path="/objects",
            query=query or None,
            resp=responses.ObjectsResponse,
        )

    async def get_object(self, object_id: int) -> responses.ObjectResponse:
        return await self.__make_request(
            method=HTTPMethod.GET,
            path=f"/objects/{object_id}",
            resp=responses.ObjectResponse,
        )

    async def list_departments(self) -> responses.DepartmentsResponse:
        return await self.__make_request(
            method=HTTPMethod.GET,
            path="/departments",
            resp=responses.DepartmentsResponse,
        )

    async def search(
        self,
        query: str,
        is_highlight: bool | None = None,
        title: bool | None = None,
        tags: bool | None = None,
        department_id: int | None = None,
        is_on_view: bool | None = None,
        artist_or_culture: bool | None = None,
        medium: Sequence[str] | None = None,
        has_images: bool | None = None,
        geo_location: Sequence[str] | None = None,
        date_begin: int | None = None,
        date_end: int | None = None,
    ) -> responses.SearchResponse:
        if (date_begin is None and date_end is not None) or (
            date_begin is not None and date_end is None
        ):
            raise ValueError("Both date_begin and date_end must be provided.")

        query_params: dict[str, str] = dict(q=query)

        if is_highlight is not None:
            query_params["isHighlight"] = "true" if is_highlight else "false"
        if title is not None:
            query_params["title"] = "true" if title else "false"
        if tags is not None:
            query_params["tags"] = "true" if tags else "false"
        if is_on_view is not None:
            query_params["isOnView"] = "true" if is_on_view else "false"
        if artist_or_culture is not None:
            query_params["artistOrCulture"] = "true" if artist_or_culture else "false"
        if medium is not None:
            query_params["medium"] = "|".join(medium)
        if department_id is not None:
            query_params["departmentId"] = str(department_id)
        if has_images is not None:
            query_params["hasImages"] = "true" if has_images else "false"
        if geo_location is not None:
            query_params["geoLocation"] = "|".join(geo_location)
        if date_begin is not None and date_end is not None:
            query_params["dateBegin"] = str(date_begin)
            query_params["dateEnd"] = str(date_end)

        return await self.__make_request(
            method=HTTPMethod.GET,
            path="/search",
            query=query_params or None,
            resp=responses.SearchResponse,
        )


__all__ = ("MetMuseum",)
