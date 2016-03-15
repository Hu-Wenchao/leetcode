"""
Given two integers representing the numerator and 
denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the 
repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign+str(quotient), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            quotient, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(quotient))
        index = stack.index(remainder)
        result.insert(index+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
