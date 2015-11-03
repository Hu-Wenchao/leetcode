"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        numlen = 0
        temp = x
        while temp > 0:
            temp = temp // 10
            numlen += 1
        if numlen < 2:
            return True
        for i in range(1, numlen/2 + 1):
            if x // 10**(numlen-1) == x % 10:
                x = (x % 10**(numlen-1)) / 10
                numlen -= 2
            else:
                return False
        return True
