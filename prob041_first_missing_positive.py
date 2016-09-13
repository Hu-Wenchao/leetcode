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
        tmp = [0] * len(nums)
        for n in nums:
            if 0 < n <= len(nums):
                tmp[n-1] = 1
        for i in xrange(len(nums)):
            if tmp[i] != 1:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from heapq import heapify, heappop
        h = [n for n in nums if n > 0]
        if not h:
            return 1
        heapify(h)
        if h[0] != 1:
            return 1
        i = 1
        while h:
            a = heappop(h)
            if a == i:
                continue
            elif a = i + 1:
                i += 1
                continue
            else:
                return i + 1
        return i + 1

