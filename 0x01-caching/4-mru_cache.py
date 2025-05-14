#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache implements an MRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_order = []  # Most recently used at the end

    def put(self, key, item):
        """ Add an item in the cache using MRU """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard most recently used item
            mru_key = self.usage_order.pop()  # Last item is most recently used
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key and mark it as recently used """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
