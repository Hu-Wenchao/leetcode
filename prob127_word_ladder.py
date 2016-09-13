"""
Given two words (beginWord and endWord), and a dictionary's 
word list, find the length of shortest transformation sequence 
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        import string
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord)
        while front:
            front = wordList & (set(word[:index] + ch + word[index+1:]
                                    for word in front
                                    for index in range(len(word))
                                    for ch in string.ascii_lowercase))
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
        return 0
