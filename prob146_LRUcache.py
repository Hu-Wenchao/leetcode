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
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v
        return v

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:
                self.dic.popitem(last=False) 
        self.dic[key] = value
