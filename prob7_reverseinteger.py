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
        flag = 1
        result = 0
        if x < 0:
            x *= -1
            flag = -1
        if x == 0:
            return 0
        while x > 0:
            result = result * 10 + x % 10
            if x > 10:
                if flag < 0 and result > (2**31 // 10):
                    return 0
                elif flag > 0 and result > (2**31 - 1) // 10:
                    return 0
            x = x // 10
        if flag < 0:
            return -1 * result
        else:
            return result
