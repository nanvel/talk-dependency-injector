from unittest.mock import Mock

from todopy.use_cases import DeleteTask


def test_delete_task():
    task_id = 0
    tasks_repository = Mock()
    use_case = DeleteTask(tasks_repository=tasks_repository)

    use_case.call(task_id=task_id)

    assert tasks_repository.delete_by_id.mock_calls[0].args[0] == task_id
