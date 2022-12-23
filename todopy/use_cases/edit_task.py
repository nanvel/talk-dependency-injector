from ..repositories import TasksRepository


class EditTask:
    def __init__(self, tasks_repository: TasksRepository):
        self.tasks_repository = tasks_repository

    def call(self, task_id: int, text: str):
        self.tasks_repository.edit(task_id=task_id, text=text)
