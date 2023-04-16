import random

from cache.cache import Cache


class Rand(Cache):
    def get_page(self, page) -> int:
        if page in self.cache:
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            self.cache.remove(random.choice(self.cache))
        self.cache.append(page)
        return 1

