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
        pptr = 0
        sptr = 0
        ss = 0
        star = -1
        while sptr < len(s):
            if pptr < len(p) and (s[sptr] == p[pptr] or p[pptr] == '?'):
                sptr += 1
                pptr += 1
                continue
            if pptr < len(p) and p[pptr] == '*':
                star = pptr
                pptr += 1
                ss = sptr
                continue
            if star != -1:
                pptr = star + 1
                ss += 1
                sptr = ss
                continue
            return False
        while pptr < len(p) and p[pptr] == '*':
            pptr += 1
        if pptr == len(p):
            return True
        return False
