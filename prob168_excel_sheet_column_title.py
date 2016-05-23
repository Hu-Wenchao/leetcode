"""
Given a positive integer, return its corresponding 
column title as appear in an Excel sheet.
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            r = (n - 1) % 26
            n = (n - 1) / 26
            res = chr(r + ord('A')) + res
        return res
