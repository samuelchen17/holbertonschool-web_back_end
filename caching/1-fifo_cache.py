#!/usr/bin/env python3
"""FIFOCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:

            first_key = next(iter(self.cache_data))

            del self.cache_data[first_key]

            print("DISCARD:", first_key)

    def get(self, key):
        if key is None:
            return None

        return self.cache_data.get(key)
