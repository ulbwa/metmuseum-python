from pydantic import BaseModel, Field

from metmuseum.types.models.object_measurements import ObjectMeasurements


class ObjectMeasurementsElement(BaseModel):
    name: str = Field(alias="elementName")
    description: str | None = Field(alias="elementDescription")
    measurements: ObjectMeasurements = Field(alias="elementMeasurements")


__all__ = ("ObjectMeasurementsElement",)
