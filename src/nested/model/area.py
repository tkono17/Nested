from sqlmodel import SQLModel, Field
from .utilities import Status


class AreaBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True)
    statusId: int = Field(index=True, default=Status.NOT_STARTED)
    createTime: str | None = Field(index=True, default=None)
    updateTime: str | None = Field(index=True, default=None)

class Area(AreaBase, table=True):
    id: int = Field(primary_key=True)

class AreaPublc(AreaBase):
    id: int

class AreaCreate(AreaBase):
    pass

class AreaUpdate(AreaBase):
    name: str | None = None
    description: str | None = None
    statusId: int | None = None
    createTime: str | None = None
    updateTime: str | None = None
