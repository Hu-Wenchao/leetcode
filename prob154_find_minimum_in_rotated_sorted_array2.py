"""
Suppose a sorted array is rotated at some pivot 
unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

    def findMin2(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]
