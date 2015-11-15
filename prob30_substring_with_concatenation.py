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
        for i in range(len(s) + 1 - words_num * words_len):
            temp_dict = {}
            j = 0
            while j < words_num:
                word = s[i+j*words_len:i+(j+1)*words_len]
                if word not in words_dict:
                    break
                if word not in temp_dict:
                    temp_dict[word] = 1
                else:
                    temp_dict[word] += 1
                if words_dict[word] < temp_dict[word]:
                    break
                j += 1
            if j == words_num:
                ret.append(i)
        return ret



    def findSubstring2(self, s, words):
        # TLE error
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        words_num = len(words)
        words_len = len(words[0])
        
        if words_num * words_len > len(s):
            return []
        ret = []

        for i in range(len(s) - words_num*words_len + 1):
            temp = []
            for word in words:
                temp.append(word)
            if self.isConcatenation(s[i:i+words_num*words_len],
                                    temp, words_len, words_num):
                ret.append(i)

        return ret
    
    def isConcatenation(self, s, temp, words_len, words_num):
        for i in range(words_num):
            if s[i*words_len:(i+1)*words_len] in temp:
                temp.remove(s[i*words_len:(i+1)*words_len])
            else:
                return False
        return True
        
