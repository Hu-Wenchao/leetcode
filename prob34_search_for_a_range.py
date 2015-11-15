"""
Given a sorted array of integers, find the starting 
and ending position of a given target value.

Your algorithm's runtime complexity must be in the 
order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            end = start
            while end + 1 < len(nums) and nums[end+1] == target:
                end += 1
        return [start, end]
