"""Given an integer (signed 32 bits), write a function 
to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = 0
        while 4**res < num:
            res += 1
        return 4**res == num

    def isPowerOfFour2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        tmp = [4**i for i in xrange(17)]
        return num in tmp
