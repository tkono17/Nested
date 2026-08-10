import os
from unittest import case
import dotenv
from typing import Callable, TypeVar, Any
import logging
from sqlmodel import create_engine
from sqlalchemy import Select

from ..service import (
    AreaRepository, ProjectRepository, TaskTypeRepository, TaskRepository, CommentRepository,
    NestedDbService
)

log = logging.getLogger(__name__)

T = TypeVar('T')
TPublic = TypeVar('TPublic')

class AppCore:
    def __init__(self):
        self.areas = []
        self.projects = []
        self.taskTypes = []
        self.tasks = []
        self.comments = []

        self.currentArea = None
        self.currentProject = None
        self.currentTaskType = None
        self.currentTask = None
        self.currentComment = None
        #
        self.init()

    def init(self):
        self.dataRepositories = {
            'Area': AreaRepository(),
            'Project': ProjectRepository(),
            'TaskType': TaskTypeRepository(),
            'Task': TaskRepository(),
            'Comment': CommentRepository(),
        }
        engine = None
        dotenv.load_dotenv()
        if 'DB_URL' in os.environ:
            db_url = os.environ['DB_URL']
            engine = create_engine(db_url, echo=True)
        self.dbService = NestedDbService(engine=engine)

    def create(self, tableName: str, keyValues: dict[str, Any]) -> Any | None:
        x = self.dbService.create(tableName, keyValues)
        return x

    def get(self, tableName: str, id: int) -> Any | None:
        x = self.dbService.get(tableName, id)
        return x

    def getall(self, tableName: str,
               selectModifer: Callable[[Select[T]], Select[T]]|None = None,
               offset: int=0, limit: int=100) -> list[Any] | None:
        v = self.dbService.getall(tableName, selectModifer=selectModifer, offset=offset, limit=limit)
        match tableName:
            case 'Area':
                self.areas = v
            case 'Project':
                self.projects = v
            case 'TaskType':
                self.taskTypes = v
            case 'Task':
                self.tasks = v
            case 'Comment':
                self.comments = v
        return v

    def update(self, tableName: str, id: int, keyValues: dict[str, Any]) -> Any | None:
        x = self.dbService.update(tableName, id, keyValues)
        return x

    def delete(self, tableName: str, id: int) -> int:
        status = self.dbService.delete(tableName, id)
        if status == 0:
            match tableName:
                case 'Area':
                    self.currentArea = None
                    self.areas = [ x for x in self.areas if x.id != id]
                case 'Project':
                    self.currentProject = None
                    self.projects = [ x for x in self.projects if x.id != id]
                case 'TaskType':
                    self.currentTaskType = None
                    self.taskTypes = [ x for x in self.taskTypes if x.id != id]
                case 'Task':
                    self.currentTask = None
                    self.tasks = [ x for x in self.tasks if x.id != id]
                case 'Comment':
                    self.currentComment = None
                    self.comments = [ x for x in self.comments if x.id != id]
        return x

    def selectArea(self, id: int):
        v = [ x for x in self.areas if x.id == id]
        if len(v) == 1:
            self.currentArea = v[0]
            return self.currentArea
        return None

    def selectProject(self, id: int):
        v = [ x for x in self.projects if x.id == id]
        if len(v) == 1:
            self.currentProject = v[0]
            return self.currentProject
        return None

    def selectTaskType(self, id: int):
        v = [ x for x in self.taskTypes if x.id == id]
        if len(v) == 1:
            self.currentTaskType = v[0]
            return self.currentTaskType
        return None
    
    def selectTask(self, id: int):
        v = [ x for x in self.tasks if x.id == id]
        if len(v) == 1:
            self.currentTask = v[0]
            return self.currentTask
        return None

    def selectComment(self, id: int):
        v = [ x for x in self.comments if x.id == id]
        if len(v) == 1:
            self.currentComment = v[0]
            return self.currentComment
        return None
