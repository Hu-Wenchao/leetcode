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
        result = 0
        for i in range(len(digits)):
            result += digits[i] * 10**(len(digits)-i-1)
        result += 1
        result = str(result)
        result_list = []
        for i in range(len(result)):
            result_list.append(int(result[i]))
        return result_list
