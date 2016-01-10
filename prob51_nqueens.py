"""
The n-queens puzzle is the problem of placing n queens on 
an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to 
the n-queens puzzle.

Each solution contains a distinct board configuration of 
the n-queens' placement, where 'Q' and '.' both indicate 
a queen and an empty space respectively.
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [0] * n
        plusdiag = [0] * (2 * n)
        minusdiag = [0] * (2 * n)
        board = [x[:] for x in [['.'] * n] * n]
        self.result = []

        self.dfs(0, n, col, plusdiag, minusdiag, board)

        return self.result

    def dfs(self, row_index, n, col, plusdiag, minusdiag, board):
        if row_index == n:
            self.result.append([''.join(x) for x in board])
            return

        for i in range(n):
            if col[i] == 0 and plusdiag[row_index+i] == 0 and \
               minusdiag[row_index-i] == 0:
                board[row_index][i] = 'Q'

                col[i] = 1
                plusdiag[row_index+i] = 1
                minusdiag[row_index-i] = 1
                
                self.dfs(row_index+1, n, col, plusdiag, minusdiag, board)

                col[i] = 0
                plusdiag[row_index+i] = 0
                minusdiag[row_index-i] = 0
                
                board[row_index][i] = '.'
