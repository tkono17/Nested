from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint
from .utilities import Status

# Task type: design, development, test, validation, bookkeeping, documentation, debug, thinking
class TaskBase(SQLModel):
    name: str
    description: str
    author: str
    projectId: int
    type: str
    statusId: int
    parentId: int | None = None
    startDate: str | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None

class Task(TaskBase, table=True):
    __table_args__ = (
        UniqueConstraint('name', 'projectId', 'parentId', name='uq_project_parent_task'),
    )
    id: Optional[int] = Field(primary_key=True, default=None)

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
    parentId: int | None = None
    startDate: str | None = None
    dueDate: str | None = None
    createTime: str | None = None
    updateTime: str | None = None

