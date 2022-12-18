import typer

from .container import Container
from .models import Priority


app = typer.Typer()
container = Container()


@app.callback()
def callback():
    """TODO app with dependency-injector."""


@app.command()
def create(text: str):
    container.init_resources()
    container.create_task().call(text=text)
    container.shutdown_resources()


@app.command(name="print")
def _print():
    container.init_resources()
    container.print_tasks().call()
    container.shutdown_resources()


@app.command()
def delete(task_id: int):
    container.init_resources()
    container.delete_task().call(task_id=task_id)
    container.shutdown_resources()


@app.command()
def set_priority(task_id: int, priority: Priority):
    container.init_resources()
    container.set_priority().call(task_id=task_id, priority=priority)
    container.shutdown_resources()
