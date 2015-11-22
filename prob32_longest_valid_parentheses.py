"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) 
parentheses substring.

For "(()", the longest valid parentheses substring is "()", 
which has length = 2.

Another example is ")()())", where the longest valid 
parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        length = 0
        lastError = -1
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    lastError = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        validTill = lastError
                    else:
                        validTill = stack[-1]
                    length = max(length, i-validTill)
        return length
