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
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while True:
            middle = (l + r) / 2
            if target == matrix[middle/n][middle%n]:
                return True
            if l >= r:
                return False
            if target < matrix[middle/n][middle%n]:
                r = middle - 1
            else:
                l = middle + 1
