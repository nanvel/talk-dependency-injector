from ..repositories import TasksRepository


class PrintTasks:
    def __init__(self, tasks_repository: TasksRepository, printer):
        self.tasks_repository = tasks_repository
        self.printer = printer

    def call(self):
        for task in self.tasks_repository.get_all():
            content = self.printer.call(task)
            print(content)
