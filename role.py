"""
Chloe, Aaron, Eric
UVU Advisor Bot

role.py
"""
from enum import Enum, auto

class Role(Enum):
    USER = auto()
    SYSTEM = auto()
    ASSISTANT = auto()

    def __str__(self):
        return self.name.lower()