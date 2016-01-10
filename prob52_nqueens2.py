"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, 
return the total number of distinct solutions.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = [0] * n
        plusdiag = [0] * (2 * n)
        minusdiag = [0] * (2 * n)
        board = [x[:] for x in [['.'] * n] * n]
        self.result = 0
        
        self.dfs(0, n, col, plusdiag, minusdiag, board)

        return self.result
        
    def dfs(self, row_index, n, col, plusdiag, minusdiag, board):
        if row_index == n:
            self.result += 1
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
