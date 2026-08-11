from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field


class TaskTypeBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True, default='')

class TaskType(TaskTypeBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)

class TaskTypePublic(TaskTypeBase):
    id: int

class TaskTypeCreate(TaskTypeBase):
    pass

class TaskTypeUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
