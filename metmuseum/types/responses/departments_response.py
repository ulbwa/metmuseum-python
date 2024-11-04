from pydantic import BaseModel, Field

from metmuseum.types import models


class DepartmentsResponse(BaseModel):
    departments: tuple[models.DepartmentElement, ...] = Field(alias="departments")


__all__ = ("DepartmentsResponse",)
