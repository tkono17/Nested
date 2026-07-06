from enum import Enum
from dataclasses import dataclass
from .utilities import Status
from .project import Project

@dataclass
class AreaStatus(Enum):
    ACTIVE = 1
    INACTIVE = 2

@dataclass
class Area:
    name: str
    description: str
    projects: list[Project]
    statusId: int

