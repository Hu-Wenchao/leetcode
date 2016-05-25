"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        l = 0
        res = len(nums) + 1
        for r, n in enumerate(nums):
            total += n
            while total >= s:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res <= len(nums) else 0
