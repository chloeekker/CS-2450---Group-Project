"""
Chloe, Aaron, Eric
UVU Advisor Bot

role.py
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from enum import Enum, auto

class Role(Enum):
    USER = auto()
    SYSTEM = auto()
    ASSISTANT = auto()

    def __str__(self):
        return self.name.lower()