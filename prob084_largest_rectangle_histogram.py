"""
Given n non-negative integers representing the histogram's bar 
height where the width of each bar is 1, find the area of 
largest rectangle in the histogram.
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        res = 0
        stack = []
        for i in xrange(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res
