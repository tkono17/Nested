from dataclasses import dataclass
import datetime

@dataclass
class Comment:
    author: str
    contents: str
    createTime: datetime.datetime
    updateTime: datetime.datetime

@dataclass
class Task:
    name: str
    description: str
    type: str
    category: str
    status: str
    subTasks: list[Task]
    comments: list[Comment]

@dataclass
class Project:
    name: str
    description: str
    tasks: list[Task]
    subProjects: list[Project]
    starteDate: datetime.date
    dueDate: datetime.date | None = None
    createTime: datetime.datetime | None = None
    updateTime: datetime.datetime | None = None

@dataclass
class Area:
    name: str
    description: str
    projects: list[Project]

