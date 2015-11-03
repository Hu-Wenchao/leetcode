"""
Design and implement a data structure for Least Recently
Used (LRU) cache. It should support the following
operations: get and set.

get(key) - Get the value (will always be positive) of
the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key
is not already present. When the cache reached its
capacity, it should invalidate the least recently
used item before inserting a new item.
"""

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_num = 0
        self.cache = {}
        self.usage = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            key_index = self.usage.index(key)
            self.usage.remove(key)
            self.usage.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if (self.key_num == self.capacity) and (key not in self.cache):
            
            del self.cache[self.usage[-1]]
            del self.usage[-1]
            self.key_num -= 1
        
        if key in self.cache:
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.insert(0, key)
        else:
            self.cache[key] = value
            self.usage.insert(0, key)
            self.key_num += 1
        
