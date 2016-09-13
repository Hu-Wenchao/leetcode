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
        length = 0
        invalid = -1
        stack = []
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    invalid = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        valid = invalid
                    else:
                        valid = stack[-1]
                    length = max(length, i-valid)
        return length
