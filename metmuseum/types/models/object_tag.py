from pydantic import AnyHttpUrl, BaseModel, Field


class ObjectTag(BaseModel):
    term: str = Field(alias="term")
    aat: AnyHttpUrl = Field(alias="AAT_URL")
    wikidata: AnyHttpUrl = Field(alias="Wikidata_URL")


__all__ = ("ObjectTag",)
