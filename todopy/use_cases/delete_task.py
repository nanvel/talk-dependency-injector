from ..repositories import TasksRepository


class DeleteTask:
    def __init__(self, tasks_repository: TasksRepository):
        self.tasks_repository = tasks_repository

    def call(self, task_id: int):
        self.tasks_repository.delete_by_id(task_id)
