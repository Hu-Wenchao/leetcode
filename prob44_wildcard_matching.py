"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pPointer = 0
        sPointer = 0
        ss = 0
        star = -1
        while sPointer < len(s):
            if pPointer < len(p) and \
               (s[sPointer] == p[pPointer] or p[pPointer] == "?"):
                sPointer += 1
                pPointer += 1
                continue
            if pPointer < len(p) and p[pPointer] == "*":
                star = pPointer
                pPointer += 1
                ss = sPointer
                continue
            if star != -1:
                pPointer = star + 1
                ss += 1
                sPointer = ss
                continue
            return False
        while pPointer < len(p) and p[pPointer] == "*":
            pPointer += 1
        if pPointer == len(p):
            return True
        return False
