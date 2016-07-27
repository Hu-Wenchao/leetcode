"""
Given two words word1 and word2, find the minimum number 
of steps required to convert word1 to word2. (each 
operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Analysis:
Use f[i][j] to represent the shortest edit distance between 
word1[0,i) and word2[0, j). Then compare the last character 
of word1[0,i) and word2[0,j), which are c and d respectively 
(c == word1[i-1], d == word2[j-1]):

if c == d, then : f[i][j] = f[i-1][j-1]

Otherwise we can use three operations to convert word1 to word2:

(a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;

(b) if we added d after c: f[i][j] = f[i][j-1] + 1;

(c) if we deleted c: f[i][j] = f[i-1][j] + 1;
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in xrange(l1 + 1)]
        for i in xrange(l1+1):
            dp[i][0] = i
        for j in xrange(l2+1):
            dp[0][j] = j
        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1,
                               dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
