import datetime

import pytest

from todopy.factories import TaskFactory
from todopy.models import Priority, Task


@pytest.fixture
def factory():
    enumerator = (i for i in range(10))
    return TaskFactory(enumerator=enumerator)


def test_task_factory_from_text(factory):
    text = "Example text"

    task = factory.from_text(text)
    assert isinstance(task, Task)
    assert task.id == 0
    assert task.text == text
    assert task.priority == Priority.LOW


def test_task_factory_from_dict(factory):
    text = "Example text"

    task = factory.from_dict(
        {
            "id": 0,
            "text": text,
            "time": datetime.datetime(2022, 1, 1, 1, 1),
            "priority": Priority.LOW,
        }
    )

    assert isinstance(task, Task)
