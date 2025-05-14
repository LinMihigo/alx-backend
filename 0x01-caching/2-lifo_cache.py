#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a LIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.stack = []  # Tracks insertion order for LIFO

    def put(self, key, item):
        """ Add an item in the cache using LIFO """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop()  # Remove last inserted key
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.stack.append(key)
        else:
            # Move key to the top if it already exists
            self.stack.remove(key)
            self.stack.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        return self.cache_data.get(key)
