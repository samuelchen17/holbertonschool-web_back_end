#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to store.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item.

        Returns:
            The value associated with the key, or None if the key
            is None or does not exist.
        """
        if key is None:
            return None

        return self.cache_data.get(key)
