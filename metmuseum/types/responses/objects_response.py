from typing import Annotated

from annotated_types import Ge, Gt
from pydantic import BaseModel, Field


class ObjectsResponse(BaseModel):
    total: Annotated[int, Ge(0)] = Field(alias="total")
    ids: tuple[Annotated[int, Gt(1)], ...] = Field(alias="objectIDs")


__all__ = ("ObjectsResponse",)
