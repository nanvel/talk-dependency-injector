import sys
from shelve import Shelf

from .base import BaseEnumerator


class SequenceEnumerator(BaseEnumerator):
    SEQUENCE_KEY = "sequence"

    def __init__(self, shelf: Shelf):
        self.shelf = shelf
        self.range = iter(range(shelf.get(self.SEQUENCE_KEY, 0) + 1, sys.maxsize))

    def __next__(self) -> int:
        i = next(self.range)
        self.shelf[self.SEQUENCE_KEY] = i
        return i
