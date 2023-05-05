from cache.cache import Cache


# FlushWhenFull
class Fwf(Cache):
    def get_page(self, page) -> int:
        if page in self.cache:
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            self.cache = []
        self.cache.append(page)
        return 1

