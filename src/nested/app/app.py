from dataclasses import dataclass

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
        pass

    def findAreas(self, name: str|None = None, 
                  includeInactive: bool = False):
        pass

    def selectArea(self, id):
        y = None
        if y is not None: self.currentArea = y
        return y

        return y

    def findProjects(self, parentId: int | None = None,
                     includeInactive: bool = False):
        pass

    def selectProject(self, id):
        y = None
        if y is not None: self.currentProject = y
        return y

    def findTasks(self, 
                  projectId: int, 
                  includeInactive: bool = False):
        pass

    def selectTask(self, id):
        y = None
        if y is not None: self.currentTask = y
        return y

    def findComments(self, 
                     taskId: int,
                     includeInactive: bool = False):
        pass

    def selectComment(self, id):
        y = None
        if y is not None: self.currentComment = y
        return y
