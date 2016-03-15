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
        if not s or ' ' not in s:
            return s
        words = []
        index1 = 0
        while ' ' in s[index1+1:]:
            index2 = s.index(' ', index1+1)
            words.append(s[index1:index2])
            index1 = index2
        words.append(s[index1:].strip(' '))
        ret = ''
        for i in range(len(words) - 1):
            word = words.pop()
            if word != ' ':
                ret += word
        ret += ' ' + words[0]
        return ret

    def reverseWords2(self, s):
        return ' '.join(reversed(s.split()))
