"""
Given numRows, generate the first numRows of Pascal's triangle.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows = 0:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            temp = [1]
            for i in range(len(ret[-1])-1):
                temp.append(ret[-1][i] + ret[-1][i+1])
            temp.append(1)
            ret.append(temp)
        return ret
