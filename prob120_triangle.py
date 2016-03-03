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
        elif len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            temp = triangle[i]
            for j in range(len(triangle[i])):
                if j == 0:
                    temp[0] += triangle[i-1][0]
                elif j == len(triangle[i]) - 1:
                    temp[-1] += triangle[i-1][-1]
                else:
                    temp[j] += min(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i] = temp
        return min(triangle[-1])
                    
