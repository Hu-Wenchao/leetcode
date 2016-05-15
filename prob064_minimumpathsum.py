"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which 
minimizes the sum of all numbers along its path.
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not grid:
            return 0

        m, n = len(nums), len(nums[0])
        
        dp = [float('inf')] * (n+1)
        dp[1] = 0

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i-1][j-1]
                
        return dp[-1]
