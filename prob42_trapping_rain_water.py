"""
Given n non-negative integers representing an 
elevation map where the width of each bar is 1, 
compute how much water it is able to trap after 
raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        peak = height.index(max(height))
        left = height[:peak]
        right = height[peak+1:]
        left_peak = peak
        right_peak = 0
        volume = 0
        while len(left) >= 2:
            second_peak = left.index(max(left))
            if left_peak - second_peak > 1:
                for i in range(second_peak+1, left_peak):
                    volume += left[second_peak] - left[i]
            left_peak = second_peak
            left = left[:second_peak]

        while len(right) >= 2:
            second_peak = right.index(max(right))
            if second_peak > 0:
                for i in range(second_peak):
                    volume += right[second_peak] - right[i]
            right = right[second_peak+1:]

        return volume

    def trap(self, height):
        # A better written code.
        n = len(height)
        if n <= 2:
            return 0
        
        maxvalue = max(height)
        maxindex = height.index(maxvalue)
        
        previousMax = 0
        count = 0
        for i in range(0, maxindex):
            if height[i] > previousMax:
                previousMax = height[i]
            count += previousMax - height[i]

        previousMax = 0
        for i in range(n-1, maxindex, -1):
            if height[i] > previousMax:
                previousMax = height[i]
            count += previousMax - height[i]
        return count
