"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.matrix = matrix
        # empty matrix case
        result = []
        if len(matrix) == 0:
            return []
        # vector cases
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                result += matrix[i]
            return result
        
        # cases where m >= 2, n >= 2
        row = len(matrix)
        column = len(matrix[0])
        for i in range(min(row//2, column//2)):
            result += self.readRect(matrix, row, column, i)
        
        last = []
        if row == column and row % 2 == 1:
            last = [self.matrix[row//2][column//2]]
        elif row > column column % 2 == 1:
            for i in range(column//2, row-column//2):
                last += [self.matrix[i][column//2]]
        elif row < column and row % 2 == 1:
            for i in range(row//2, column-row//2):
                last += [self.matrix[row//2][i]]
        result += last
        return result

    def readRect(self, matrix, row, column, n):
        temprow1 = matrix[n][n:(column-n)]
        tempcolumn2 = []
        tempcolumn1 = []
        for i in range(n+1, row-n-1):
            tempcolumn2 += [matrix[i][column-n-1]]
            tempcolumn1 += [matrix[i][n]]
        temprow2 = matrix[row-n-1][n:(column-n)]
        temprow2.reverse()
        tempcolumn1.reverse()
        return temprow1 + tempcolumn2 + temprow2 + tempcolumn1
