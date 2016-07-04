"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up 
or down. You may NOT move diagonally or move outside of the boundary 
(i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: 
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(self.dfs(matrix, dp, m, n, i, j)
                   for i in range(m) for j in range(n))
        
    def dfs(self, matrix, dp, m, n, i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                self.dfs(matrix, dp, m, n, i - 1, j)
                if i and val > matrix[i - 1][j] else 0,
                self.dfs(matrix, dp, m, n, i + 1, j)
                if i < m - 1 and val > matrix[i + 1][j] else 0,
                self.dfs(matrix, dp, m, n, i, j - 1)
                if j and val > matrix[i][j - 1] else 0,
                self.dfs(matrix, dp, m, n, i, j + 1)
                if j < n - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]
