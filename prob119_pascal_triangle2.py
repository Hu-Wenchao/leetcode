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
        if rowIndex == 0:
            return [1]
        ret = [1]
        for i in range(rowIndex):
            temp = [1]
            for i in range(len(ret)-1):
                temp.append(ret[i] + ret[i+1])
            temp.append(1)
            ret = temp
        return ret
