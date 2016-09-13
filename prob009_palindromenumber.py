"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):
        tmp = x
        rx = 0
        while tmp > 0:
            rx = 10 * rx + tmp % 10
            tmp /= 10
        return x == rx
