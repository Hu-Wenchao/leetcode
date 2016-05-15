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
        n = len(matrix)
        for i in xrange(n / 2):
            for j in xrange(n - 1 - 2 * i):
                matrix[i+j][n-i-1], \
                matrix[n-i-1][n-i-1-j],\
                matrix[n-i-1-j][i], \
                matrix[i][i+j] = \
                                 matrix[i][i+j], \
                                 matrix[i+j][n-i-1], \
                                 matrix[n-i-1][n-i-1-j], \
                                 matrix[n-i-1-j][i]
                                                     
