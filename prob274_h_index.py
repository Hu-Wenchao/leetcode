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

    def hIndex2(self, citations):
        if not citations:
            return 0
        cites = [0] * (len(citations) + 1)
        for i in range(len(citations)):
            if citations[i] > len(citations):
                cites[-1] += 1
            else:
                cites[citations[i]] += 1
        temp = 0
        ret = 0
        for i in range(len(citations), 0, -1):
            temp += cites[i]
            if temp >= i:
                return i
        return 0
