"""
Given a triangle, find the minimum path sum from 
top to bottom. Each step you may move to adjacent 
numbers on the row below.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        for i in xrange(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in xrange(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
