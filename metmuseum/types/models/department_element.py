from typing import Annotated

from annotated_types import Gt
from pydantic import BaseModel, Field


class DepartmentElement(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="departmentId")
    display_name: str = Field(alias="displayName")


__all__ = ("DepartmentElement",)
