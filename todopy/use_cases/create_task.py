from ..factories import TaskFactory
from ..repositories import TasksRepository


class CreateTask:
    def __init__(self, tasks_repository: TasksRepository, task_factory: TaskFactory):
        self.tasks_repository = tasks_repository
        self.tasks_factory = task_factory

    def call(self, text):
        task = self.tasks_factory.from_text(text=text)

        self.tasks_repository.insert(task=task)
