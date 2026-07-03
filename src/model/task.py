from dataclasses import dataclass
from .utilities import Date

@dataclass
class Task:
    name: str
    projectId: int
    creator: str
    assignee: str | None = None
    description: str = ''
    createdDate: Date
    dueDate: Date
