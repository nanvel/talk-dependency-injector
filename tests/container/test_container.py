from todopy.container import Container
from todopy.models import Priority


def test_container(capfd):
    container = Container()

    shelf = {}
    with container.tasks_shelf.override(shelf):
        text0 = 'Task 0'
        text1 = 'Task 1'

        print_tasks = container.print_tasks()
        print_tasks.call()

        out, err = capfd.readouterr()
        assert out == ""

        create_task = container.create_task()
        create_task.call(text=text0)
        create_task.call(text=text1)
        print_tasks.call()

        out, err = capfd.readouterr()
        assert text0 in out
        assert text1 in out

        delete_task = container.delete_task()
        delete_task.call(task_id=0)
        print_tasks.call()

        out, err = capfd.readouterr()
        assert text0 not in out
        assert text1 in out

        set_priority = container.set_priority()
        set_priority.call(task_id=1, priority=Priority.MEDIUM)
        print_tasks.call()

        out, err = capfd.readouterr()
        assert '1: Task 1 [1' in out
