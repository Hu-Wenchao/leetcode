"""
Given a 2D board containing 'X' and 'O', capture 
all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's 
in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        stack = [(i, 0) for i in range(m)] + [(i, n-1) for i in range(m)]
        stack += [(0, j) for j in range(1, n-1)] + \
                 [(m-1, j) for j in range(1, n-1)]
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                stack.append((i-1, j))
                stack.append((i+1, j))
                stack.append((i, j+1))
                stack.append((i, j-1))
        board[:] = [['XO'[node=='S'] for node in row] for row in board]
