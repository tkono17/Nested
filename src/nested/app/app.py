from dataclasses import dataclass
from ..service import (
    AreaRepository, ProjectRepository, TaskTypeRepository, TaskRepository, CommentRepository
)

class App:
    def __init__(self):
        self.areas = []
        self.projects = []
        self.tasks = []
        self.comments = []
        self.currentArea = None
        self.currentProject = None
        self.currentTask = None
        self.currentComment = None
        #
        self.dataRepositories = {
            'Area': AreaRepository(),
            'Project': ProjectRepository(),
            'TaskType': TaskTypeRepository(),
            'Task': TaskRepository(),
            'Comment': CommentRepository(),
        }
        pass

    def findAreas(self, name: str|None = None, 
                  includeInactive: bool = False):
        pass

    def selectArea(self, id):
        y = None
        if y is not None: self.currentArea = y
        return y

    def findProjects(self,
                     areaId: int | None = None,
                     includeInactive: bool = False):
        pass

    def selectProject(self, id):
        y = None
        if y is not None: self.currentProject = y
        return y

    def findTasks(self, 
                  projectId: int | None = None, 
                  taskId: int | None = None, 
                  includeInactive: bool = False):
        pass

    def selectTask(self, id):
        y = None
        if y is not None: self.currentTask = y
        return y

    def findComments(self, 
                     taskId: int | None = None,
                     includeInactive: bool = False):
        pass

    def selectComment(self, id):
        y = None
        if y is not None: self.currentComment = y
        return y
