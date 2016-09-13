"""
Given a string array words, find the maximum value 
of length(word[i]) * length(word[j]) where the two 
words do not share common letters. You may assume 
that each word will contain only lower case letters. 
If no such two words exist, return 0.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        mask = [0] * len(words)
        for i in xrange(len(words)):
            for c in words[i]:
                mask[i] |= 1 << (ord(c) - ord('a'))
        res = 0
        for i in xrange(len(words)):
            for j in xrange(i+1, len(words)):
                if mask[i] & mask[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
