"""
Write an efficient algorithm that searches for a 
value in an m x n matrix. This matrix has the 
following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the 
last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return target in matrix[i]
        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1
        
        while True:
            middle = (left + right) / 2
            if target == matrix[middle/n][middle%n]:
                return True
            if left >= right:
                return False
            if target < matrix[middle/n][middle%n]:
                right = middle - 1
            else:
                left = middle + 1

    def searchMatrix3(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False
        
        # find the correct row
        row = 0
        for i in range(m):
            if target <= matrix[i][-1]:
                row = i
                break

        # find the correct column
        for i in range(n):
            if target == matrix[row][i]:
                return True
        
        return False
