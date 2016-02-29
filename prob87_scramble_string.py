"""
Given a string s1, we may represent it as a binary tree 
by partitioning it to two non-empty substrings recursively.
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if s1 == s2 or len(s1) < 4:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[i:], s2[i:]) and \
               self.isScramble(s1[:i], s2[:i]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and \
               self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
