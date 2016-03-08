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
        s = ''
        while n > 0:
            t = (n - 1) % 26
            n = (n - 1) / 26
            s = chr(t + ord('A')) + s
        return s
