from pydantic import BaseModel, Field


class ObjectMeasurements(BaseModel):
    heigth: float | None = Field(alias="Height", default=None)
    width: float | None = Field(alias="Width", default=None)
    diameter: float | None = Field(alias="Diameter", default=None)


__all__ = ("ObjectMeasurements",)
