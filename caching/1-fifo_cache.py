#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching"""

    def __init__(self):
        """init FIFO cache and track insert order"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add item to cache using FIFO"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(0)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """given key return value from cache"""
        if key is None:
            return None

        return self.cache_data.get(key)
