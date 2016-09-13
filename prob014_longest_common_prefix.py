"""
Write a function to find the longest common
prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = strs[0]
        for s in strs[1:]:
            res = self.compre(res, s)
        return res
        
    def compre(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        for i in xrange(len(s1), -1, -1):
            if s1[:i] == s2[:i]:
                return s1[:i]
