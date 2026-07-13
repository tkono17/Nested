from dataclasses import dataclass
from enum import IntEnum
import re

@dataclass
class Date:
    text: str

    def decode(self) -> tuple[int, int, int] | None:
        y = None
        mg = re.search(r'([\d]{4})-([\d]{2})-([\d]{2})', self.text)
        if mg is not None:
            y = mg.groups()
        return y
    
    def encode(self, y, m, d):
        self.text = f'{y:02d}-{m:02d}-{d:02d}'

@dataclass
class Time:
    text: str

    def decode(self) -> tuple[int, int]:
        mg = re.search(r'([\d]{2}):([\d]{2}):([\d]{2})', self.text)
        if mg is not None:
            y = mg.groups()
        return y
    
    def encode(self, h, m, s):
        self.text = f'{h:02d}:{m:02d}:{s:02d}'


class DateTime:
    text: str

    def decode(self) -> tuple[Date, Time]:
        y = None
        mg = re.search('([\d-]+)T([\d:]+)')
        if mg is not None:
            d, t = mg.groups()
            y = (Date(d), Time(t))
        return y

@dataclass
class Status(IntEnum):
    NOT_STARTED = 1
    ACTIVE = 2
    DONE = 3
    INVALID = 4
    TERMINATED = 5
