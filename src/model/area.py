from dataclasses import dataclass

@dataclass
class Area:
    name: str
    projects: list[Project]
    