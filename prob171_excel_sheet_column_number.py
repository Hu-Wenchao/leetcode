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
        ret = 0
        for i in range(len(s)):
            ret = ret * 26 + ord(s[i]) - ord('A') + 1
        return ret
