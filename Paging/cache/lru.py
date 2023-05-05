from cache.cache import Cache


# LeastRecentlyUsed
class Lru(Cache):
    def get_page(self, page) -> int:
        if page in self.cache:
            self.cache.remove(page)
            self.cache.append(page)
            return 0

        # page not in cache
        if len(self.cache) == self.k:
            self.cache.pop(0)
        self.cache.append(page)
        return 1


