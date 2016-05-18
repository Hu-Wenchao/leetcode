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
        words = []
        while ' ' in s:
            index = s.index(' ')
            words.append(s[:index])
            s = s[index:].strip(' ')
        words.append(s)
        return ' '.join(words[::-1])

    def reverseWords2(self, s):
        return ' '.join(reversed(s.split()))
