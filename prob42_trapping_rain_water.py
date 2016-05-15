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
        if len(height) < 3:
            return 0
        peak = height.index(max(height))
        left = height[:peak]
        right = height[peak+1:]
        left_peak = peak
        right_peak = 0
        ret = 0
        while len(left) >= 2:
            second_peak = left.index(max(left))
            if left_peak - second_peak > 1:
                for i in xrange(second_peak+1, left_peak):
                    ret += left[second_peak] - left[i]
            left_peak = second_peak
            left = left[:left_peak]
        while len(right) >= 2:
            second_peak = right.index(max(right))
            if second_peak > 0:
                for i in xrange(second_peak):
                    ret += right[second_peak] - right[i]
            right = right[second_peak+1:]
        return ret

    def trap2(self, height):
        if len(height) < 3:
            return 0
        peakid = height.index(max(height))

        prepeak = 0
        ret = 0
        for i in xrange(peakid):
            if height[i] > prepeak:
                prepeak = height[i]
            ret += prepeak - height[i]

        prepeak = 0
        for i in xrange(len(height)-1, peakid, -1):
            if height[i] > prepeak:
                prepeak = height[i]
            ret += prepeak - height[i]
        return ret
