from datetime import datetime

from pydantic import BaseModel

from .priority import Priority


class Task(BaseModel):
    id: int
    text: str
    priority: Priority
    time: datetime
