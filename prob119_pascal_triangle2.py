"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        while rowIndex > 1:
            res = [1] + [res[i-1] + res[i] for i in xrange(1, len(res))] + [1]
            rowIndex -= 1
        return res
