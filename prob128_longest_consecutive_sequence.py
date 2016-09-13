"""
Given an unsorted array of integers, find the length of 
the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. 
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxlen = 0
        while nums:
            n = nums.pop()
            right = 0
            left = 0
            i = n + 1
            while i in nums:
                nums.remove(i)
                i += 1
                right += 1
            i = n - 1
            while i in nums:
                nums.remove(i)
                i -= 1
                left += 1
            maxlen = max(maxlen, left + right + 1)
        return maxlen
