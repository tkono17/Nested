from enum import Enum
from dataclasses import dataclass
from .utilities import Date, DateTime

@dataclass
class TaskType:
    name: str
    description: str

@dataclass
class Comment:
    author: str
    contents: str
    taskId: int
    createTime: DateTime
    updateTime: DateTime

# Task type: design, development, test, validation, bookkeeping, documentation, debug, thinking
@dataclass
class Task:
    name: str
    description: str
    author: str
    type: str
    statusId: int
    parentProjectId: int
    parentTaskId: int | None = None
    startDate: Date | None = None
    dueDate: Date | None = None
    createTime: DateTime | None = None
    updateTime: DateTime | None = None
