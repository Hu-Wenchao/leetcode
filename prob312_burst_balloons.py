"""
Given n balloons, indexed from 0 to n-1. Each balloon 
is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst 
balloon i you will get nums[left] * nums[i] * nums[right] 
coins. Here left and right are adjacent indices of i. After 
the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the 
balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not 
real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [n for n in nums if n > 0] + [1]
        dp = [[0] * len(nums) for _ in xrange(len(nums))]
        for k in xrange(2, len(nums)):
            for left in xrange(0, len(nums) - k):
                right = left + k
                for i in xrange(left + 1,right):
                    dp[left][right] = max(dp[left][right], nums[left] * \
                                          nums[i] * nums[right] + \
                                          dp[left][i] + dp[i][right])
        return dp[0][len(nums) - 1]        
            
