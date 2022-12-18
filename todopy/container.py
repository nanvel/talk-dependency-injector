from dependency_injector import containers, providers

from .enumerators import SequenceEnumerator, TimeEnumerator
from .factories import TaskFactory
from .printers import CsvPrinter, TextPrinter
from .repositories import TasksRepository
from .resources import init_tasks_shelf
from .settings import Settings
from .use_cases import CreateTask, DeleteTask, PrintTasks, SetPriority


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(pydantic_settings=[Settings()])

    tasks_shelf = providers.Resource(init_tasks_shelf, db_path=config.db_path)

    time_enumerator = providers.Singleton(TimeEnumerator)
    sequence_enumerator = providers.Singleton(SequenceEnumerator, shelf=tasks_shelf)

    task_factory = providers.Singleton(TaskFactory, enumerator=sequence_enumerator)

    tasks_repository = providers.Singleton(
        TasksRepository, shelf=tasks_shelf, task_factory=task_factory
    )

    csv_printer = providers.Singleton(CsvPrinter, delimiter=",")
    text_printer = providers.Singleton(TextPrinter, color=config.text_color)

    create_task = providers.Factory(
        CreateTask, tasks_repository=tasks_repository, task_factory=task_factory
    )
    delete_task = providers.Factory(DeleteTask, tasks_repository=tasks_repository)
    print_tasks = providers.Factory(
        PrintTasks, tasks_repository=tasks_repository, printer=text_printer
    )
    set_priority = providers.Factory(SetPriority, tasks_repository=tasks_repository)
