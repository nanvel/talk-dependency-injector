from unittest.mock import Mock

import pytest

from todopy.factories import TaskFactory
from todopy.models import Task
from todopy.use_cases import CreateTask


@pytest.fixture
def task_factory():
    enumerator = (i for i in range(10))
    return TaskFactory(enumerator=enumerator)


def test_create_task(task_factory):
    text = "Example text"
    tasks_repository = Mock()
    use_case = CreateTask(tasks_repository=tasks_repository, task_factory=task_factory)

    use_case.call(text=text)

    assert isinstance(tasks_repository.insert.mock_calls[0].kwargs["task"], Task)
