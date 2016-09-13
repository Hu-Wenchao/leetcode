"""
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1 
            r -= 1
        return True

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        for c in s:
            if c.isalnum():
                tmp.append(c.lower())
        return tmp == tmp[::-1]
