from unittest.mock import Mock

from todopy.models import Priority
from todopy.use_cases import SetPriority


def test_set_priority():
    task_id = 0
    tasks_repository = Mock()
    use_case = SetPriority(tasks_repository=tasks_repository)

    use_case.call(task_id=task_id, priority=Priority.HIGH)

    tasks_repository.set_priority.assert_called_once()
    call = tasks_repository.set_priority.mock_calls[0]
    assert call.kwargs['task_id'] == task_id
    assert call.kwargs['priority'] == Priority.HIGH
