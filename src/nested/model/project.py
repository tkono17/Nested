from enum import Enum
from sqlmodel import SQLModel, Field
from .utilities import Status

class ProjectBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True)
    areaId: int = Field(index=True)
    statusId: int = Field(index=True, default=Status.NOT_STARTED)
    startDate: str | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None
