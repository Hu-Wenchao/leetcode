"""
Given two numbers represented as strings, return multiplication
 of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            reutn '0'
        m = len(num1)
        n = len(num2)
        ret = [0] * (m + n)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) *\
                      (ord(num2[j]) - ord('0'))
                ret[i+j+1] += mul % 10
                ret[i+j] += mul / 10
        for i in xrange(m+n-1, 0, -1):
            if ret[i] > 9:
                ret[i-1] += ret[i] / 10
                ret[i] %= 10
        return ''.join([str(item) for item in ret]).lstrip('0')
