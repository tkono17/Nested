from __future__ import annotations
from sqlalchemy import Engine

import appbasics as apb
from ..model import (
    Area, AreaBase, AreaPublic, AreaCreate, AreaUpdate,
    Project, ProjectBase, ProjectPublic, ProjectCreate, ProjectUpdate,
    TaskType, TaskTypeBase, TaskTypePublic, TaskTypeCreate, TaskTypeUpdate,
    Task, TaskBase, TaskPublic, TaskCreate, TaskUpdate,
    Comment, CommentBase, CommentPublic, CommentCreate, CommentUpdate,
)

class AreaRepository(apb.TableAccess):
    def __init__(self):
        super().__init__('area', Area, AreaPublic, AreaCreate, AreaUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class ProjectRepository(apb.TableAccess):
    def __init__(self):
        super().__init__('project', Project, ProjectPublic, ProjectCreate, ProjectUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class TaskTypeRepository(apb.TableAccess):
    def __init__(self):
        super().__init__('tasktype', TaskType, TaskTypePublic, TaskTypeCreate, TaskTypeUpdate)

    def getByName(self, name: str, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.name == name)
        return self.get(engine, modifier)
    pass

class TaskRepository(apb.TableAccess):
    def __init__(self):
        super().__init__('task', Task, TaskPublic, TaskCreate, TaskUpdate)

    def getByProjectId(self, projectId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.projectId == projectId)
        return self.get(engine, modifier)

    def getByParentTaskId(self, parentTaskId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.parentTaskId == parentTaskId)
        return self.get(engine, modifier)
    pass

class CommentRepository(apb.TableAccess):
    def __init__(self):
        super().__init__('comment', Comment, CommentPublic, CommentCreate, CommentUpdate)

    def getByTaskId(self, taskId: int, engine: Engine):
        def modifier(statement):
            return statement.where(self.TDb.taskId == taskId)
        return self.get(engine, modifier)
    pass
