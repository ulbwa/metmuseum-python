from typing import Annotated

from annotated_types import Gt
from pydantic import AnyHttpUrl, BaseModel, Field


class ObjectConstituent(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="constituentID")
    role: str
    name: str
    ulan: AnyHttpUrl = Field(alias="constituentULAN_URL")
    gender: str


__all__ = ("ObjectConstituent",)
