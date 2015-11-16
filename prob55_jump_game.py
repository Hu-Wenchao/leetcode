"""
Given an array of non-negative integers, you are 
initially positioned at the first index of the array.

Each element in the array represents your maximum 
jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 1
        while i < reach and reach < len(nums):
            reach = max(reach, i + 1 + nums[i])
            i += 1
        return reach >= len(nums)

    def canJump2(self, nums):
        n = len(nums)
        if n == 0:
            return True
        leftmost = n - 1
        i = n - 2
        while i >= 0:
            if i + nums[i] >= leftmost:
                leftmost = i
            i -= 1
        return leftmost == 0

    def canJump3(self, nums):
        f = [0] * len(nums)
        for i in range(1, len(nums)):
            f[i] = max(f[i-1], nums[i-1]) - 1
            if f[i] < 0:
                return False
        return f[len(nums)-1] >= 0 
