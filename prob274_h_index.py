"""
Given an array of citations (each citation is a 
non-negative integer) of a researcher, write a 
function to compute the researcher's h-index.
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
        return i + 1

