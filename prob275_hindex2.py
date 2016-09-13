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
        l, h = 0, n - 1
        while l <= h:
            m = (l + h) / 2
            if n - m <= citations[m]:
                h = m - 1
            else:
                l = m + 1
        return n - l
