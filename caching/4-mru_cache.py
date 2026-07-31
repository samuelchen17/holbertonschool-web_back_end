#!/usr/bin/env python3
"""MRU caching module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cashing class"""

    def __init__(self):
        """init cache and track keys"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add item to cache using MRU"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.order.pop(-2)
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """given key return value from cache"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
