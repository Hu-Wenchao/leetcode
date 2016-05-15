"""
You are given a string, s, and a list of words,
words, that are all of the same length. Find
all starting indices of substring(s) in s that
is a concatenation of each word in words exactly 
once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution(object):
    def indSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_dict = {}
        words_num = len(words)
        words_len = len(words[0])
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        ret = []
        for i in xrange(len(s) - words_num * words_len + 1):
            j = 0
            tmp_dict = {}
            while j < words_num:
                word = s[i+j*words_len : i+(j+1)*words_len]
                if word not in words_dict:
                    break
                if word not in tmp_dict:
                    tmp_dict[word] = 1
                else:
                    tmp_dict[word] += 1
                if tmp_dict[word] > words_dict[word]:
                    break
                j += 1
            if j == words_num:
                ret.append(i)
        return ret
