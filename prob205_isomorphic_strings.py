"""
Given two strings s and t, determine if they are isomorphic.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)

    
    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}
        for i in xrange(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = t[i]
            elif dic_s[s[i]] != t[i]:
                return False
            if t[i] not in dic_t:
                dic_t[t[i]] = s[i]
            elif dic_t[t[i]] != s[i]:
                return False
        return True
