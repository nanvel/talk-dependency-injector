from abc import ABC, abstractmethod

from ..models import Task


class BasePrinter(ABC):
    @abstractmethod
    def call(self, task: Task) -> str:
        ...
