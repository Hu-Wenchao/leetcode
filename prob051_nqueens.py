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
        res = []
        self.dfs(n, [], [], [], res)
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in sol] for sol in res]

    def dfs(self, n, queens, xy_dif, xy_sum, res):
        p = len(queens)
        if p == n:
            res.append(queens)
            return
        for q in xrange(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                self.dfs(n, queens+[q], xy_dif+[p-q], xy_sum+[p+q], res)
