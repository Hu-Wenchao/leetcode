"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        value_a = 0
        value_b = 0
        for i in range(len(a)):
            value_a += int(a[i]) * 2**(len(a)-i-1)
        for i in range(len(b)):
            value_b += int(b[i]) * 2**(len(b)-i-1)
        result = value_a + value_b
        return bin(result)[2:]
