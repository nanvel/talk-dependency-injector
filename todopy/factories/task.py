from datetime import datetime
from typing import Generator

import pytz

from ..models import Task, Priority


class TaskFactory:
    def __init__(self, enumerator: Generator[int, None, None]):
        self.enumerator = enumerator

    def from_dict(self, data: dict) -> Task:
        return Task(**data)

    def from_text(self, text: str) -> Task:
        return Task(
            id=next(self.enumerator),
            text=text,
            time=datetime.utcnow().replace(tzinfo=pytz.UTC),
            priority=Priority.LOW,
        )
