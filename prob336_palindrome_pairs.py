"""
Given a list of unique words. Find all pairs of distinct 
indices (i, j) in the given list, so that the concatenation 
of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wordict = {}
        res = []
        for i in range(len(words)):
            wordict[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]] != i and \
                   tmp2 == tmp2[::-1]:
                    res.append([i, wordict[tmp1[::-1]]])
                if j != 0 and tmp2[::-1] in wordict and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]], i])
        return res
