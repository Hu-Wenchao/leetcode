"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x > 0:
            res = 10 * res + x % 10
            x /= 10
        return sign * res if -2**31 <= sign * res <= 2**31 - 1 else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        res = int(str(abs(x))[::-1])
        return sign * res if -2**31 <= sign * res <= 2**31 - 1 else 0
