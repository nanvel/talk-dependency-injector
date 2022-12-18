import shelve

from pydantic.types import FilePath


def init_tasks_shelf(db_path: FilePath):
    with shelve.open(str(db_path)) as shelf:
        yield shelf
