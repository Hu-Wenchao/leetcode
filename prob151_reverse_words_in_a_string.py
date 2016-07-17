"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(' ')
        s = s.split(' ')
        while '' in s:
            s.remove('')
        return ' '.join(s[::-1])
