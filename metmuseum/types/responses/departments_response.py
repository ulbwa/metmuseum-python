from pydantic import BaseModel, Field

from metmuseum.types.models.department_element import DepartmentElement


class DepartmentsResponse(BaseModel):
    departments: tuple[DepartmentElement, ...] = Field(alias="departments")


__all__ = ("DepartmentsResponse",)
