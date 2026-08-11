from __future__ import annotations
from sqlalchemy import Engine
from functools import partial
from appbasics import RdbAccess

from .repositories import (
    AreaRepository,
    ProjectRepository,
    TaskTypeRepository,
    TaskRepository,
    CommentRepository,
)

class NestedDbService(RdbAccess):
    def __init__(self, engine: Engine = None):
        super().__init__()
        self.engine = engine
        self.init()

    def init(self):
        self.tables['area'] = AreaRepository()
        self.tables['project'] = ProjectRepository()
        self.tables['tasktype'] = TaskTypeRepository()
        self.tables['task'] = TaskRepository()
        self.tables['comment'] = CommentRepository()

        self.getAreaByName = partial(self.tables['area'].getByName, engine=self.engine)
        self.getProjectByName = partial(self.tables['project'].getByName, engine=self.engine)
        self.getTaskTypeByName = partial(self.tables['tasktype'].getByName, engine=self.engine)
        self.getTaskByProjectId = partial(self.tables['task'].getByProjectId, engine=self.engine)
        self.getTaskByParentId = partial(self.tables['task'].getByParentId, engine=self.engine)
        self.getCommentByTaskId = partial(self.tables['comment'].getByTaskId, engine=self.engine)
