"""
Given two arrays of length m and n with digits 0-9 representing 
two numbers. Create the maximum number of length k <= m + n from 
digits of the two. The relative order of the digits from the same 
array must be preserved. Return an array of the k digits. You 
should try to optimize your time and space complexity.
"""

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        return max(self.merge(self.prepare(nums1, i), self.prepare(nums2, k-i))
                   for i in xrange(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))
    
    def prepare(self, nums, k):
        # Find the maximum number with (len(nums) - k) digits
        # in nums while keep the relative digit position unchanged.
        drop = len(nums) - k
        res = []
        for num in nums:
            while drop and res and res[-1] < num:
                res.pop()
                drop -= 1
            res.append(num)
        return res[:k]
        
    def merge(self, a, b):
        return [max(a, b).pop(0) for _ in a + b]
