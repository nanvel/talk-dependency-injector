from unittest.mock import Mock

from todopy.use_cases import PrintTasks


def test_print_tasks(capfd):
    task = Mock()
    tasks_repository = Mock()
    tasks_repository.get_all.return_value = [task]
    content = 'example content'
    printer = Mock()
    printer.call.return_value = content
    use_case = PrintTasks(tasks_repository=tasks_repository, printer=printer)

    use_case.call()

    out, err = capfd.readouterr()
    assert out == f"{content}\n"
