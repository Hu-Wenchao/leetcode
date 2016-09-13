"""
You are climbing a stair case. It takes n steps 
to reach to the top.

Each time you can either climb 1 or 2 steps. In 
how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in xrange(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
