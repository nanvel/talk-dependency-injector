import csv
from io import StringIO

from .base import BasePrinter

from ..models import Task


class CsvPrinter(BasePrinter):
    def __init__(self, delimiter: str):
        self.delimiter = delimiter

    def call(self, task: Task) -> str:
        f = StringIO()
        writer = csv.writer(f, delimiter=self.delimiter)
        writer.writerow([task.id, task.text, task.priority, task.time])
        return f.getvalue().strip()
