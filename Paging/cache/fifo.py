from cache.cache import Cache


class Fifo(Cache):
    def get_page(self, page) -> int:
        if page in self.cache:
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            self.cache.pop(0)
        self.cache.append(page)
        return 1

