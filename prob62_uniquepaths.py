"""
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Based on combination theory, result = (m+n-2)! / (m-1)! / (n-1)!
        return self.factorial(m+n-2) / self.factorial(m-1) / self.factorial(n-1)
        
    def factorial(self, n):
        ret = 1
        for i in range(n):
            ret *= i + 1
        return ret     
        

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]     
        return dp[-1]
