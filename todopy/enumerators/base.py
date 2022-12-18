from abc import ABC, abstractmethod


class BaseEnumerator(ABC):
    @abstractmethod
    def __next__(self) -> int:
        ...
