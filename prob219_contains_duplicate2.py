"""
Given an array of integers and an integer k, find out 
whether there are two distinct indices i and j in the 
array such that nums[i] = nums[j] and the difference 
between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if n not in dic:
                dic[n] = i
            else:
                if i - dic[n] <= k:
                    return True
                dic[n] = i
        return False
