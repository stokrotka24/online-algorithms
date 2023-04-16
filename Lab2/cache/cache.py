from abc import ABC, abstractmethod


class Cache(ABC):
    k: int
    cache: list[int]

    def __init__(self, k: int):
        self.k = k
        self.cache = []

    @abstractmethod
    def get_page(self, page) -> int:
        pass
