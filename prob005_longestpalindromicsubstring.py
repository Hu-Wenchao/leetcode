"""
Given a string S, find the longest palindromic 
substring in S. You may assume that the maximum
length of S is 1000, and there exists one unique
longest palindromic substring.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, l = 0, 0
        for i in xrange(len(s)):
            if i - l >= 1 and s[i-l-1 : i+1] == s[i-l-1 : i+1][::-1]:
                start = i - l - 1
                l += 2   
            elif s[i-l : i+1] == s[i-l : i+1][::-1]:
                start = i - l
                l += 1
        return s[start : start+l]
            
