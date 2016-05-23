"""
Given an integer n, return the number of trailing zeroes in n!.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5 factors in range n+1 to 5n is n
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
