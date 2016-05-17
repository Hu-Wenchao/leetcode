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
        if numRows <= 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        while numRows > 2:
            res.append([1] + [res[-1][i-1] + res[-1][i]
                              for i in xrange(1, len(res[-1]))] + [1])
            numRows -= 1
        return res
