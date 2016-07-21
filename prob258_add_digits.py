"""
Given a non-negative integer num, repeatedly add all its digits 
until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return 1 + ((num - 1) % 9)

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num /= 10
            num = tmp
        return num
