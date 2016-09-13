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
        len_s, len_p = len(s), len(p)
        i, j, star_match_pos, last_star_pos = 0, 0, 0, -1
        while i < len_s:
            if j < len_p and p[j] in (s[i], '?'):
                i, j = i + 1, j + 1
            # when meet a '*', first assume it will match 0 character in s
            elif j < len_p and p[j] == '*':
                star_match_pos, last_star_pos = i, j
                j += 1
            # now p[j] is not ?, not *, can't match s[i], we can only
            # use the last '*'
            elif last_star_pos > -1:
                i, star_match_pos = star_match_pos + 1, star_match_pos + 1
                j = last_star_pos + 1
            else:
                return False
        while j < len_p and p[j] == '*':
            j += 1
        return j == len_p
