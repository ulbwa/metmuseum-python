from typing import Annotated

from annotated_types import MinLen
from pydantic import BaseModel, Field, field_validator


class ObjectTag(BaseModel):
    term: str = Field(alias="term")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    aat: Annotated[str, MinLen(1)] | None = Field(alias="AAT_URL")
    wikidata: Annotated[str, MinLen(1)] | None = Field(alias="Wikidata_URL")

    @field_validator("aat", "wikidata", mode="before")
    def validate_empty_str_as_none(cls, v: str) -> str | None:
        if v == "":
            return None
        return v


__all__ = ("ObjectTag",)
