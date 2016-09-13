"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine 
the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if (c == ')' and tmp != '(') or \
                   (c == ']' and tmp != '[') or \
                   (c == '}' and tmp != '{'):
                    return False
        return len(stack) == 0
                    
