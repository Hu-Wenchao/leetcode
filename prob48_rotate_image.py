"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(len(matrix) / 2):
            num1 = i
            num2 = n - i
            for j in range(num1, num2):
                temp = matrix[num1][j]
                matrix[num1][j] = matrix[n-j][num1]
                matrix[n-j][num1] = matrix[num2][n-j]
                matrix[num2][n-j] = matrix[j][num2]
                matrix[j][num2] = temp
        return
