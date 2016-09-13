"""
Given an array of integers, find out whether there are two 
distinct indices i and j in the array such that the difference 
between nums[i] and nums[j] is at most t and the difference 
between i and j is at most k.
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        d = {}
        t += 1
        for i in xrange(len(nums)):
            if i > k:
                del d[nums[i - k - 1] / t]
            m = nums[i] / t
            if m in d:
                return True
            elif m - 1 in d and abs(nums[i] - d[m - 1]) < t:
                return True
            elif m + 1 in d and abs(nums[i] - d[m + 1]) < t:
                return True
            d[m] = nums[i]
        return False
