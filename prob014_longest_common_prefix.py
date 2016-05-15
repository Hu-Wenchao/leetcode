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
        if len(strs) == 0:
            return ''
        com = strs[0]
        for i in xrange(1, len(strs)):
            com = self.helper(com, strs[i])
        return com
        
    def helper(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        i = len(s1)
        while i > 0:
            if s1[:i] == s2[:i]:
                return s1[:i]
            i -= 1
        return ''
