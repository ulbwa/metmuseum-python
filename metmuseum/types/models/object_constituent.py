from typing import Annotated

from annotated_types import Gt
from pydantic import BaseModel, Field, field_validator


class ObjectConstituent(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="constituentID")
    role: str = Field(alias="role")
    name: str = Field(alias="name")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    ulan: str | None = Field(alias="constituentULAN_URL")

    gender: str = Field(alias="gender")

    @field_validator("ulan", mode="before")
    def validate_empty_str_as_none(cls, v):
        if v == "":
            return None
        return v


__all__ = ("ObjectConstituent",)
