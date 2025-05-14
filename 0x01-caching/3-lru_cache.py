#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache implements an LRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)  # Remove so we can re-add to the end

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove least recently used item
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key and update its usage """
        if key is None or key not in self.cache_data:
            return None

        # Mark key as recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
