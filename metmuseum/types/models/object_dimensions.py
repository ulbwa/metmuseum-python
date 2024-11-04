from pydantic import BaseModel, Field


class ObjectDimensions(BaseModel):
    element: str = Field(alias="element")
    dimension_type: str = Field(alias="dimensionType")
    dimension: float = Field(alias="dimension")


__all__ = ("ObjectDimensions",)
