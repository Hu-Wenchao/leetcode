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
        b, e = 0, x
        while b < e:
            m = (b + e + 1) / 2
            if m**2 == x:
                return m
            elif m**2 < x:
                b = m
            else:
                e = m - 1
        return b
