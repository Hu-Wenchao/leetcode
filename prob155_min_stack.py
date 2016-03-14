"""
Design a stack that supports push, pop, top, and 
retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][-1])))
        
    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack[-1][-1]
