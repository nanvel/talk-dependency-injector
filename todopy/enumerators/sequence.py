import sys

from .base import BaseEnumerator


class SequenceEnumerator(BaseEnumerator):
    SEQUENCE_KEY = "sequence"

    def __init__(self, shelf: dict):
        self.shelf = shelf
        self.range = iter(range(shelf.get(self.SEQUENCE_KEY, -1) + 1, sys.maxsize))

    def __next__(self) -> int:
        i = next(self.range)
        self.shelf[self.SEQUENCE_KEY] = i
        return i
