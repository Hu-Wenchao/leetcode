"""
Given an array and a value, remove all instances of 
that value in place and return the new length.

The order of elements can be changed. It doesn't matter 
what you leave beyond the new length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l
    
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

    def removeElement3(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] != val:
                i += 1
            else:
                del nums[i]
        return len(nums)
