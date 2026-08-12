from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint
from .utilities import Date, DateTime


class CommentBase(SQLModel):
    taskId: int = Field(index=True)
    number: int = Field(index=True)
    author: str = Field(index=True)
    contents: str = Field(index=True)
    format: str = Field(index=True, default='text')
    createTime: str = Field(index=True, default='')
    updateTime: str = Field(index=True, default='')

class Comment(CommentBase, table=True):
    __table_args__ = (
        UniqueConstraint('taskId', 'number', name='uq_task_number'),
    )
    id: Optional[int] = Field(primary_key=True, default=None)

class CommentPublic(CommentBase):
    id: int

class CommentCreate(CommentBase):
    pass

class CommentUpdate(SQLModel):
    taskId: int | None = None
    number: int | None = None
    author: str | None = None
    contents: str | None = None
    format: str | None = None
    createTime: str | None = None
    updateTime: str | None = None
