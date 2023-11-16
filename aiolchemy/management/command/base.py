"""
Base commands for usage
"""
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """
    Abstract command
    """
    name = None
    
    def __init__(self, args) -> None:
        self.args = args

    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class NullCommand(BaseCommand):
    """
    Command with null execution
    """
    def execute(self):
        return None


class ErrorCommand(BaseCommand):
    def execute(self):
        raise
