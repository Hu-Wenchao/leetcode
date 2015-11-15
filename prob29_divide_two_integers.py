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
        isNegative = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            count <<= 1
        result = 0
        while dividend > 0 and divisor >= 1:
            if dividend >= divisor:
                dividend -= divisor
                result += count
            divisor >>= 1
            count >>= 1
        if isNegative:
            return max(-result, -2147483648)
        else:
            return min(result, 2147483647)
