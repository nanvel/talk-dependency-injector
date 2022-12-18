from ..models import Priority
from ..repositories import TasksRepository


class SetPriority:
    def __init__(self, tasks_repository: TasksRepository):
        self.tasks_repository = tasks_repository

    def call(self, task_id: int, priority: Priority):
        self.tasks_repository.set_priority(task_id=task_id, priority=priority)
