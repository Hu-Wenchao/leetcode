"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing all ones 
and return its area.
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        mat = [[0] * w for _ in range(h)]
        for i in xrange(h):
            for j in xrange(w):
                if mattrix[i][j] == '1':
                    mat[i][j] = mat[i-1][j] + 1
        return max(self.largestRectangleArea(row) for row in mat)

    def largestRectangleArea(self, height):
        height.append(0)
        ret = 0
        stack = []
        for i in xrange(len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                ret = max(ret, h * w)
            stack.append(i)
        return ret
