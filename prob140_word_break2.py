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

    def findwords(self, start, end, s, wordDict, res):
        if start in res:
            return res[start]
        res[start] = []
        candidate = ''
        cur = start
        while cur < end:
            candidate += s[cur]
            cur += 1
            if candidate in wordDict:
                if cur == end:
                    res[start].append(candidate)
                else:
                    for x in self.findwords(cur, end, s, wordDict, res):
                        res[start].append(candidate + ' ' + x)
        return res[start]
