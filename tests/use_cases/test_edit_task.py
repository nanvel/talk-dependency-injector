from unittest.mock import Mock

from todopy.use_cases import EditTask


def test_edit_task():
    task_id = 0
    text = "Edited"
    tasks_repository = Mock()
    use_case = EditTask(tasks_repository=tasks_repository)

    use_case.call(task_id=task_id, text=text)

    tasks_repository.edit.assert_called_once()
    call = tasks_repository.edit.mock_calls[0]
    assert call.kwargs["task_id"] == task_id
    assert call.kwargs["text"] == text
