from pydantic import BaseModel, Field


class ObjectMeasurements(BaseModel):
    heigth: float = Field(alias="Height")
    width: float = Field(alias="Width")


__all__ = ("ObjectMeasurements",)
