#!/usr/bin/env python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cashing class"""

    def __init__(self):
        """init cache and track insert order"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add item to cache using LIFO"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(-2)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """given key return value from cache"""
        if key is None:
            return None

        return self.cache_data.get(key)
