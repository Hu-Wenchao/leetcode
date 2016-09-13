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
        if not words or not s:
            return []
        word_dic = {}
        word_num = len(words)
        word_len = len(words[0])
        for w in words:
            if w not in word_dic:
                word_dic[w] = 1
            else:
                word_dic[w] += 1
        res = []
        for i in xrange(len(s) - word_num * word_len + 1):
            j = 0
            tmp_dic = {}
            while j < word_num:
                w = s[i+j*word_len : i+(j+1)*word_len]
                if w not in word_dic:
                    break
                if w not in tmp_dic:
                    tmp_dic[w] = 1
                else:
                    tmp_dic[w] += 1
                if tmp_dic[w] > word_dic[w]:
                    break
                j += 1
            if j == word_num:
                res.append(i)
        return res
