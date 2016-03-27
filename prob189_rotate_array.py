"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the 
array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
