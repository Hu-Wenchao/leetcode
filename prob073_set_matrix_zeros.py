"""
Given a m x n matrix, if an element is 0, set its 
entire row and column to 0. Do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [1] * m, [1] * n
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in xrange(m):
            for j in xrange(n):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        return
