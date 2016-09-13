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
        if not nums:
            return 0
        premax = nums[0]
        premin = nums[0]
        res = nums[0]
        for n in nums[1:]:
            curmax = max(n, max(premax * n, premin * n))
            curmin = min(n, min(premax * n, premin * n))
            res = max(res, curmax)
            premax = curmax
            premin = curmin
        return res
