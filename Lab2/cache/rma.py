import random

from cache.cache import Cache


# RandomizedMarkingAlgorithm
class Rma(Cache):
    marked_up: dict[int, bool]

    def __init__(self, k: int):
        self.marked_up = dict()
        super().__init__(k)

    def get_page(self, page) -> int:
        if page in self.cache:
            self.marked_up[page] = True
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            if all(self.marked_up.values()):
                for p in self.marked_up:
                    self.marked_up[p] = False

            p = random.choice([p for p, marked_up in self.marked_up.items() if not marked_up])
            self.cache.remove(p)
            del self.marked_up[p]

        self.cache.append(page)
        self.marked_up[page] = True
        return 1

