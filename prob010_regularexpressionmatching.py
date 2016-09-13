"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # define the state dp[i][j] to be true
        # if p[0..i) matches s[0..j) and false otherwise.
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in xrange(n + 1)]
        dp[0][0] = True
        for i in xrange(1, n+1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in xrange(1, m+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or \
                               (dp[i-1][j-1] and p[i-2] == s[j-1]) or \
                               (dp[i][j-1] and p[i-2] == '.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[n][m]
            
