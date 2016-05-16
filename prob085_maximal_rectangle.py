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
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i-1][j] + 1
        return max(self.helper(row) for row in dp)

    def helper(self, height):
        height.append(0)
        res = 0
        stack = []
        for i in xrange(len(height)):
            while stack and height[i]< height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res
