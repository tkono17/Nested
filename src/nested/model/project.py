from enum import Enum
from dataclasses import dataclass
from .utilities import Date, DateTime


@dataclass
class Project:
    name: str
    description: str
    author: str
    areaId: int
    statusId: int
    startDate: Date | None = None
    dueDate: Date | None = None
    createTime: DateTime | None = None
    updateTime: DateTime | None = None
