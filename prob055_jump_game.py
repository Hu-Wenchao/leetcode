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
        left = right = 0
        while left <= right:
            old_right = right
            for i in xrange(left, old_right+1):
                new_right = max(right, i+nums[i])
                if new_right >= len(nums)-1:
                    return True
                if new_right > right:
                    right = new_right
            left = old_right + 1
        return False
