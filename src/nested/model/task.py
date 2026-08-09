from enum import Enum
from sqlmodel import SQLModel, Field
from .utilities import Status

# Task type: design, development, test, validation, bookkeeping, documentation, debug, thinking
class TaskBase:
    name: str
    description: str
    author: str
    type: str
    statusId: int
    projectId: int
    parentTaskId: int | None = None
    startDate: str | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None

class Task(TaskBase, table=True):
    id: int = Field(primary_key=True)

class TaskPublic(TaskBase):
    id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    author: str | None = None
    type: str | None = None
    statusId: int | None = None
    projectId: int | None = None
    parentTaskId: int | None = None
    startDate: str | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None

