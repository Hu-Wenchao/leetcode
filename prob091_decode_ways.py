"""
A message containing letters from A-Z is being encoded to 
numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine 
the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded 
as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # w tells the number of ways
        # v tells the previous number of ways
        # d is the current digit
        # p is the previous digit
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w
