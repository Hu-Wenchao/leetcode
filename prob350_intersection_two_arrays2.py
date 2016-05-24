"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for n in nums1:
            if n in nums2:
                nums2.remove(n)
                res.append(n)
        return res
