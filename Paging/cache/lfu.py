from collections import Counter

from cache.cache import Cache


# LeastFrequentlyUsed
class Lfu(Cache):
    counter: Counter

    def __init__(self, k: int):
        self.counter = Counter()
        super().__init__(k)

    def get_page(self, page) -> int:
        self.counter[page] += 1

        if page in self.cache:
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            p, _ = sorted([(p, self.counter[p]) for p in self.cache], key=lambda x: x[1])[0]
            self.cache.remove(p)
        self.cache.append(page)
        return 1


