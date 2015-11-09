"""
There are two sorted arrays nums1 and nums2 of size m
and n respectively. Find the median of the two sorted
arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        if ((m + n) % 2 != 0):
            return self.findKth(nums1, nums2, (m + n) / 2, 0, m-1, 0, n-1)
        else:
            return (self.findKth(nums1, nums2, (m + n) / 2, 0, m-1, 0, n-1) +
                    self.findKth(nums1, nums2, (m + n) / 2 - 1, 0,
                                 m-1, 0, n-1)) * 0.5
        
    def findKth(self, nums1, nums2, k, aStart, aEnd, bStart, bEnd):
        aLen = aEnd - aStart + 1
        bLen = bEnd - bStart + 1
        
        if aLen == 0:
            return nums2[bStart + k]
        elif bLen == 0:
            return nums1[aStart + k]
        elif k == 0 and nums1[aStart] < nums2[bStart]:
            return nums1[aStart]
        elif k == 0 and nums1[aStart] >= nums2[bStart]:
            return nums2[bStart]

        aMid = aLen * k / (aLen + bLen)
        bMid = k - aMid - 1

        aMid = aMid + aStart
        bMid = bMid + bStart

        if (nums1[aMid] > nums2[bMid]):
            k = k - (bMid - bStart + 1)
            aEnd = aMid
            bStart = bMid + 1
        else:
            k = k - (aMid - aStart + 1)
            bEnd = bMid
            aStart = aMid + 1

        return self.findKth(nums1, nums2, k, aStart, aEnd, bStart, bEnd)
