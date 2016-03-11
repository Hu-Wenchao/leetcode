"""
Follow up for H-Index: What if the citations array 
is sorted in ascending order? Could you optimize your algorithm?
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) / 2
            if n - mid <= citations[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return n - low
