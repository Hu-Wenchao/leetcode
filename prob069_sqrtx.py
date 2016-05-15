"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        begin = 0
        end = x
        while begin < end:
            mid = begin + (end - begin + 1) / 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                begin = mid
            else:
                end = mid - 1
        return begin
