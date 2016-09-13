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
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and j > 0 and nums1[i] < nums2[j-1]:
                imin = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays2(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l / 2)
        else:
            return (self.kth(nums1, nums2, l / 2) + 
                    self.kth(nums1, nums2, l / 2 - 1)) / 2.0
            
    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        ia, ib = len(nums1) / 2, len(nums2) / 2
        ma, mb = nums1[ia], nums2[ib]       
        if ia + ib < k:
            if ma > mb:
                return self.kth(nums1, nums2[ib+1:], k - ib - 1)
            else:
                return self.kth(nums1[ia+1:], nums2, k - ia - 1)
        else:
            if ma > mb:
                return self.kth(nums1[:ia], nums2, k)
            else:
                return self.kth(nums1, nums2[:ib], k)
            
