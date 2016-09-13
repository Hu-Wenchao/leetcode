"""
Given a 2D board and a list of words from the dictionary, 
find all words in the board.

Each word must be constructed from letters of sequentially 
adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not be 
used more than once in a word.
"""

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        res = set()
        used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '', used, res)
        return list(res)
        
    def find(self, board, i, j, trie, pre, used, res):
        if '#' in trie:
            res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not used[i][j] and board[i][j] in trie:
            used[i][j] = True
            self.find(board, i+1, j, trie[board[i][j]],
                      pre+board[i][j], used, res)
            self.find(board, i-1, j, trie[board[i][j]],
                      pre+board[i][j], used, res)
            self.find(board, i, j+1, trie[board[i][j]],
                      pre+board[i][j], used, res)
            self.find(board, i, j-1, trie[board[i][j]],
                      pre+board[i][j], used, res)
            used[i][j] = False
            return
