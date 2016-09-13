"""
Given a string S and a string T, count the number of 
distinct subsequences of T in S.

A subsequence of a string is a new string which is 
formed from the original string by deleting some 
(can be none) of the characters without disturbing 
the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1, l2 = len(s)+1, len(t)+1
        dp = [[1] * l2 for _ in xrange(l1)]
        for j in xrange(1, l2):
            dp[0][j] = 0
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
        return dp[-1][-1]
