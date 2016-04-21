"""
Suppose a sorted array is rotated at some pivot
unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found 
in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        # Find the smallest element using binary serarch.
        while l < r:
            m = (l + r) / 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # The rotation point.
        rot = l
        l, r = 0, len(nums) - 1
        # Binary search take rotation shift into consideration.
        while l <= r:
            m = (l + r) / 2
            rm = (m + rot) % len(nums)
            if nums[rm] == target:
                return realmid
            if nums[rm] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
