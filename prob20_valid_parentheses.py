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
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                preOpen = stack.pop()
                if (s[i] == ")" and preOpen != "(") or \
                   (s[i] == "]" and preOpen != "[") or \
                   (s[i] == "}" and preOpen != "{"):
                    return False
        return len(stack) == 0
