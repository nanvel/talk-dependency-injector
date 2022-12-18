import time

from .base import BaseEnumerator


class TimeEnumerator(BaseEnumerator):
    def __next__(self) -> int:
        return int(time.monotonic() * 1000)
