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
        curmax = 0
        while words:
            curword = set(words[0])
            curlen = len(words[0])
            words = words[1:]
            for word in words:
                for char in curword:
                    if char in word:
                        break
                else:
                    curmax = max(curmax, curlen*len(word))
        return curmax
            
