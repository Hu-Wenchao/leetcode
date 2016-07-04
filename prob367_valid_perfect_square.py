"""
Given a positive integer num, write a function which returns True 
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        b, e = 1, (num >> 1) + 1
        while b <= e:
            mid = (b + e) >> 1
            sq = mid * mid
            if sq == num:
                return True
            if sq > num:
                e = mid - 1
            else:
                b = mid + 1
        return False
