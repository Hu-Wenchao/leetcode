"""
Calculate the sum of two integers a and b, but you are 
not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        import ctypes
        sum = 0
        carry = ctypes.c_int32(b)
        while carry.value != 0:
            sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = sum
        return sum
