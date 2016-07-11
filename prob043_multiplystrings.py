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
        res = [0] * (m + n)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) *\
                      (ord(num2[j]) - ord('0'))
                res[i+j+1] += mul % 10
                res[i+j] += mul / 10
        for i in xrange(m+n-1, 0, -1):
            if res[i] > 9:
                res[i-1] += res[i] / 10
                res[i] %= 10
        return ''.join([str(item) for item in res]).lstrip('0')
