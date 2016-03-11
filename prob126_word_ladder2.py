"""
Given two words (beginWord and endWord), and a dictionary's 
word list, find all shortest transformation sequence(s) 
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""
from collections import defaultdict
import string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlen = len(beginWord)
        front, back = defaultdict(list), defaultdict(list)
        front[beginWord].append([beginWord])
        back[endWord].append([endWord])
        wordlist.discard(beginWord)
        if endWord not in wordlist:
            wordlist.add(endWord)
        forward, result = True, []
        while front:
            nextSet = defaultdict(list)
            for word, paths in front.items():
                for index in range(wordlen):
                    for ch in string.ascii_lowercase:
                        nextWord = word[:index] + ch + word[index+1:]
                        if nextWord in wordlist:
                            if forward:
                                nextSet[nextWord].extend([path + [nextWord] 
                                                          for path in paths])
                            else:
                                nextSet[nextWord].extend([[nextWord] + path 
                                                          for path in paths])
            front = nextSet
            common = set(front) & set(back)
            if common:
                if not forward:
                    front, back = back, front
                result.extend([head + tail[1:] for word in common 
                               for head in front[word] 
                               for tail in back[word]])
                return result
            
            if len(front) > len(back):
                front, back, forward = back, front, not forward

            wordlist -= set(front)
        return []
                                
