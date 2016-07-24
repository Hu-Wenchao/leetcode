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
        nums.sort()
        res = sum(nums[:3])
        gap = abs(res - target)
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                tmp_target = target - nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == tmp_target:
                        return target
                    elif s < tmp_target:
                        if tmp_target - s < gap:
                            gap = tmp_target - s
                            res = s + nums[i]
                        l += 1
                    else:
                        if s - tmp_target < gap:
                            gap = s - tmp_target
                            res = s + nums[i]
                        r -= 1
        return res
