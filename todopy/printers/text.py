from pydantic.color import Color
from termcolor import colored

from .base import BasePrinter
from ..models import Task


class TextPrinter(BasePrinter):
    def __init__(self, color: Color):
        self.color = color

    def call(self, task: Task) -> str:
        return colored(
            f"{task.id}: {task.text} [{task.priority} {task.time}]",
            self.color.as_named(),
        )
