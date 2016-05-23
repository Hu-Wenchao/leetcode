"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, 
return its corresponding column number.
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = res * 26 + ord(c) - ord('A') + 1
        return res
