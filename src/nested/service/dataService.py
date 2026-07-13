from __future__ import annotations
from ..model import AreaCreate, AreaPublic

class AreaService:
    def __init__(self):
        pass

    def addArea(self, x: AreaCreate):
        pass

    def findAreas(self, onlyActive: bool = True) -> list[AreaPublic]:
        pass

    def selectArea(self, id: int) -> AreaPublic | None:
        pass

class ProjectService:
    def __init__(self):
        pass

    def addProject(self, x: ProjectCreate):
        pass

    def findProjects(self, onlyActive: bool = True):
        pass

    def selectProject(self, id: int):
        pass

class TaskTypeService:
    pass

class TaskService:
    pass

class CommentService:
    pass
