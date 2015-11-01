"""
Given an array S of n integers, find three integers in S 
such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that 
each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return
        nums.sort()
        result = sum(nums[0:3])
        gap = abs(result - target)
        for i in range(0, len(nums)-2):
            new_target = target - nums[i]
            start = i + 1
            end = len(nums) - 1
            if i == 0 or nums[i] > nums[i-1]:
                while(start < end):
                    if nums[start] + nums[end] == new_target:
                        result = target
                        return result
                    elif nums[start] + nums[end] < new_target:
                        new_gap = abs(nums[start] + nums[end] - new_target)
                        if new_gap < gap:
                            gap = new_gap
                            result = nums[start] + nums[end] + nums[i]
                        start += 1
                    else:
                        new_gap = abs(nums[start] + nums[end] - new_target)
                        if new_gap < gap:
                            gap = new_gap
                            result = nums[start] + nums[end] + nums[i]
                        end -= 1
        return result
