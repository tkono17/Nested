from enum import Enum
from sqlmodel import SQLModel, Field


class TaskTypeBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True, default='')

class TaskType(TaskTypeBase, table=True):
    id: int = Field(primary_key=True)

class TaskTypePublic(TaskTypeBase):
    id: int

class TaskTypeCreate(TaskTypeBase):
    pass

class TaskTypeUpdate(TaskTypeBase):
    name: str | None = None
    description: str | None = None
    
