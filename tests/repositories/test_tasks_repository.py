from datetime import datetime

import pytest

from todopy.factories import TaskFactory
from todopy.models import Priority, Task
from todopy.repositories import TasksRepository


@pytest.fixture
def task():
    return Task(
        id=0,
        text="Lorem ipsum",
        time=datetime(2022, 1, 1, 1, 1),
        priority=Priority.LOW,
    )


@pytest.fixture
def repository():
    shelf = {}
    enumerator = (i for i in range(10))
    task_factory = TaskFactory(enumerator=enumerator)
    return TasksRepository(shelf=shelf, task_factory=task_factory)


def test_empty_repository(repository):
    assert repository.get_all() == []


def test_insert(repository, task):
    repository.insert(task)

    (task,) = repository.get_all()
    assert task.id == 0


def test_delete_by_id(repository, task):
    task_id = 1
    assert task_id != task.id

    repository.insert(task)
    repository.insert(
        Task(
            id=task_id,
            text="Lorem ipsum",
            time=datetime(2022, 1, 1, 1, 1),
            priority=Priority.LOW,
        )
    )
    assert len(repository.get_all()) == 2

    repository.delete_by_id(task_id)

    assert len(repository.get_all()) == 1


def test_set_priority(repository, task):
    repository.insert(task)

    repository.set_priority(task_id=task.id, priority=Priority.HIGH)

    (task,) = repository.get_all()
    assert task.priority == Priority.HIGH
