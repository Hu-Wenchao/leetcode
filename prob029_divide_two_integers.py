"""
Divide two integers without using multiplication, 
division and mod operator.

If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res, c = 0, 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            c <<= 1
        while c >= 1:
            if dividend >= divisor:
                dividend -= divisor
                res += c
            divisor >>= 1
            c >>= 1
        if sign == -1:
            res = -res
        return min(max(res, -2**31), 2**31 - 1)
