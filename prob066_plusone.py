"""
Given a non-negative number represented as an array of digits,
 plus one to the number.

The digits are stored such that the most significant digit is
at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0, 0)
        digits[-1] += 1
        for i in xrange(len(digits)-1, 0, -1):
            digits[i-1] += digits[i] / 10
            digits[i] %= 10
        if digits[0] == 0:
            return digits[1:]
        return digits
