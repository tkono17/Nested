from enum import Enum
from sqlmodel import SQLModel, Field
from .utilities import Status

class ProjectBase(SQLModel):
    name: str = Field(index=True)
    areaId: int = Field(index=True)
    description: str = Field(index=True, default='')
    parentId: id | None = Field(index=True, default=None)
    statusId: int = Field(index=True, default=Status.NOT_STARTED)
    startDate: str | None = Field(index=True, default=None)
    dueDate: str | None = Field(index=True, default=None)
    createTime: str | None = Field(index=True, default=None)
    updateTime: str | None = Field(index=True, default=None)

class Project(ProjectBase, table=True):
    id: int = Field(primary_key=True)

class ProjectPublic(ProjectBase):
    id: int

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(SQLModel):
    name: str|None = None
    areaId: int|None = None
    description: str|None = None
    parentId: int|None = None
    statusId: int|None = None
    startDate: str|None | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None
