from sqlmodel import SQLModel
from .utilities import Date, DateTime


@dataclass
class Comment(SQLModel):
    author: str
    contents: str
    taskId: int
    createTime: DateTime
    updateTime: DateTime
