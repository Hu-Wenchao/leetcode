"""
Given an Iterator class interface with methods: next() 
and hasNext(), design and implement a PeekingIterator 
that support the peek() operation -- it essentially peek() 
at the element that will be returned by the next call to next().
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.peekVal = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peekVal = self.iterator.next()
            self.peeked = True
        return self.peekVal

    def next(self):
        """
        :rtype: int
        """
        if not self.peeked:
            return self.iterator.next()
        else:
            self.peeked = False
            return self.peekVal

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.peeked

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
