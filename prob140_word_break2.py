"""
Given a string s and a dictionary of words dict, 
add spaces in s to construct a sentence where each 
word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.findwords(0, len(s), s, wordDict, {})

    def findwords(self, start, end, s, wordDict, cache):
        if start in cache:
            return cache[start]
        cache[start] = []
        candidate = ''
        current = start
        while current < end:
            candidate += s[current]
            current += 1
            if candidate in wordDict:
                if current == end:
                    cache[start].append(candidate)
                else:
                    for x in self.findwords(current, end, s, wordDict, cache):
                        cache[start].append(candidate + ' ' + x)
        return cache[start]
