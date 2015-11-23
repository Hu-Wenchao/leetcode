"""
Given an unsorted integer array, find the first missing 
positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        m = max(nums)
        if m <= 0:
            return 1
        temp = list(range(1, m+2))
        print(temp)
        for i in range(n):
            if nums[i] > 0:
                temp[nums[i]-1] = 0
        print(temp)
        for i in range(m+1):
            if temp[i] != 0:
                return i + 1
