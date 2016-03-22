"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak 
element and return its index.

The array may contain multiple peaks, in that case return t
he index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and 
your function should return the index number 2.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return nums.index(max(nums))
        if not nums:
            return
        nums = [float('-inf')] + nums + [float('-inf')]
        for i in range(1, len(nums)-1):
           if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
               return i-1

    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right
