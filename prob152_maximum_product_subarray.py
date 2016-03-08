"""
Find the contiguous subarray within an array (containing at 
least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxherepre = nums[0]
        minherepre = nums[0]
        maxsofar = nums[0]
        for i in range(1, len(nums)):
            maxhere = max(max(maxherepre*nums[i], minherepre*nums[i]), nums[i])
            minhere = min(min(maxherepre*nums[i], minherepre*nums[i]), nums[i])
            maxsofar = max(maxsofar, maxhere)
            maxherepre = maxhere
            minherepre = minhere
        return maxsofar
