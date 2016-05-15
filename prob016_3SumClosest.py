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
        result = sum(nums[:3])
        gap = abs(result - target)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                newTarget = target - nums[i]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == newTarget:
                        return target
                    elif s < newTarget:
                        newGap = abs(s - newTarget)
                        if newGap < gap:
                            gap = newGap
                            result = s + nums[i]
                        l += 1
                    else:
                        newGap = abs(s - newTarget)
                        if newGap < gap:
                            gap = newGap
                            result = s + nums[i]
                        r -= 1
        return result
