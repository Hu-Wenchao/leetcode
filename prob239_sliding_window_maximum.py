"""
Given an array nums, there is a sliding window of size k 
which is moving from the very left of the array to the 
very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = []
        for i, n in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue = queue[1:]
            while queue and nums[queue[-1]] < n:
                queue.pop()
            queue.append(i)
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res
