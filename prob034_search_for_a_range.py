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
        s = self.binsearch(nums, target - 0.5)
        if nums[s] != target:
            return [-1, -1]
        nums.append(float('inf'))
        e = self.binsearch(nums, target + 0.5)
        return [s, e-1]


    def binsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if target < nums[m]:
                r = m
            else:
                l = m + 1
        return l

    def searchRange2(self, nums, target):
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return res
        else:
            res[0] = l
        r = len(nums) - 1
        while l < r:
            m = (l + r) / 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        res[1] = r
        return res
