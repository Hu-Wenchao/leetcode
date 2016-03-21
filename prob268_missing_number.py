"""
Given an array containing n distinct numbers taken 
from 0, 1, 2, ..., n, find the one that is missing 
from the array.

For example,
Given nums = [0, 1, 3] return 2.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [False] * (len(nums) + 1)
        for term in nums:
            temp[term] = True
        for i in xrange(len(temp)):
            if not temp[i]:
                return i

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ret = len(nums)
        
        for i in range(ret):
            ret ^= nums[i]
            ret ^= i
            i += 1
        return ret

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)
