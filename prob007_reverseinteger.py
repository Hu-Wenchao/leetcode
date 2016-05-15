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
        ret = 0
        while x > 0:
            ret = 10 * ret + x % 10
            x //= 10
        return sign * ret if ret < 2**31 - 1 else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        ret = int(str(abs(x))[::-1])
        return sign * ret if ret < 2**31 - 1 else 0
