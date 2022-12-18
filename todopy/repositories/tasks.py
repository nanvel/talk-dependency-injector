from typing import Generator
from operator import attrgetter

from ..factories import TaskFactory
from ..models import Priority, Task


class TasksRepository:
    TASKS_KEY = "tasks"

    def __init__(self, shelf: dict, task_factory: TaskFactory):
        if not shelf.get(self.TASKS_KEY):
            shelf[self.TASKS_KEY] = []

        self.shelf = shelf
        self.task_factory = task_factory

    def tasks(self) -> Generator[Task, None, None]:
        for task_dict in self.shelf.get(self.TASKS_KEY):
            yield self.task_factory.from_dict(task_dict)

    def get_all(self) -> [Task]:
        return list(sorted(self.tasks(), key=attrgetter("priority"), reverse=True))

    # commands
    def insert(self, task: Task) -> None:
        self.shelf[self.TASKS_KEY] = self.shelf[self.TASKS_KEY] + [task.dict()]

    def delete_by_id(self, task_id: int) -> None:
        self.shelf[self.TASKS_KEY] = [
            task.dict() for task in self.tasks() if task.id != task_id
        ]

    def set_priority(self, task_id: int, priority: Priority) -> None:
        for n, task in enumerate(self.tasks()):
            if task.id == task_id:
                task.priority = priority
                self.shelf[self.TASKS_KEY] = (
                    self.shelf[self.TASKS_KEY][:n]
                    + [task.dict()]
                    + self.shelf[self.TASKS_KEY][n + 1 :]
                )
                break
