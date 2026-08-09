from sqlmodel import SQLModel, Field
from .utilities import Date, DateTime


class CommentBase(SQLModel):
    author: str = Field(index=True)
    contents: str = Field(index=True)
    taskId: int = Field(index=True)
    format: str = Field(index=True, default='text')
    createTime: str = Field(index=True, default='')
    updateTime: str = Field(index=True, default='')

class Comment(CommentBase, table=True):
    id: int = Field(primary_key=True)

class CommentPublic(CommentBase):
    id: int

class CommentCreate(CommentBase):
    pass

class CommentUpdate(SQLModel):
    author: str | None = None
    contents: str | None = None
    taskId: int | None = None
    createTime: str | None = None
    updateTime: str | None = None
