from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint
from .utilities import Status

class AreaBase(SQLModel):
    name: str = Field(index=True)
    domain: str = Field(index=True)
    description: str = Field(index=True, default='')
    createTime: str | None = Field(index=True, default=None)
    updateTime: str | None = Field(index=True, default=None)

class Area(AreaBase, table=True):
    __table_args__ = (
        UniqueConstraint('name', 'domain', name='uq_domain_area'),
    )
    id: Optional[int] = Field(primary_key=True, default=None)

class AreaPublic(AreaBase):
    id: int

class AreaCreate(AreaBase):
    pass

class AreaUpdate(SQLModel):
    name: str | None = None
    domain: str | None = None
    description: str | None = None
    createTime: str | None = None
    updateTime: str | None = None
