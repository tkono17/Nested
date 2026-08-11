from __future__ import annotations
from sqlalchemy import Engine

import appbasics as apb
from ..model import (
    Area, AreaPublic, AreaCreate, AreaUpdate,
    Project, ProjectPublic, ProjectCreate, ProjectUpdate,
    TaskType, TaskTypePublic, TaskTypeCreate, TaskTypeUpdate,
    Task, TaskPublic, TaskCreate, TaskUpdate,
    Comment, CommentPublic, CommentCreate, CommentUpdate,
)

class AreaRepository(apb.TableAccess):
    def __init__(self):
        super().__init__(Area, AreaPublic, AreaCreate, AreaUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class ProjectRepository(apb.TableAccess):
    def __init__(self):
        super().__init__(Project, ProjectPublic, ProjectCreate, ProjectUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class TaskTypeRepository(apb.TableAccess):
    def __init__(self):
        super().__init__(TaskType, TaskTypePublic, TaskTypeCreate, TaskTypeUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class TaskRepository(apb.TableAccess):
    def __init__(self):
        super().__init__(Task, TaskPublic, TaskCreate, TaskUpdate)

    def getByProjectId(self, projectId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.projectId == projectId)
        return self.get(engine, modifier)

    def getByParentId(self, parentId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.parentId == parentId)
        return self.get(engine, modifier)
    pass

class CommentRepository(apb.TableAccess):
    def __init__(self):
        super().__init__(Comment, CommentPublic, CommentCreate, CommentUpdate)

    def getByTaskId(self, taskId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.taskId == taskId)
        return self.get(engine, modifier)
    pass
