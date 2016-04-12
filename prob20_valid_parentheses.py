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
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if (ch == ')' and x != '(') or \
                   (ch == ']' and x != '[') or \
                   (ch == '}' and x != '{'):
                    return False
        return len(stack) == 0
                    
