"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to 
the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 
and 0 respectively in the grid.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * (n+1)
        dp[1] = 1
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[j] = (dp[j] + dp[j-1]) if obstacleGrid[i-1][j-1]==0 else 0
        return dp[-1]
                        
        
