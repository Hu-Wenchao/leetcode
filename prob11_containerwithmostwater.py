"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis
forms a container, such that the container
contains the most water.

Note: You may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        i = 0
        j = n - 1
        maxResult = 0
        while i < j:
            maxResult = max(maxResult, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxResult
            
    
    def maxArea2(self, height):
        # TLE error
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        else:
            container = []
            for i in range(n):
                temp = []
                for j in range(n):
                    if i < j:
                        temp.append(abs(i - j) * min(height[i], height[j]))
                    else:
                        temp.append(0)
                container.append(list(temp))
        
        max_volume = []
        for i in range(n):
            max_volume.append(max(container[i]))
        
        return max(max_volume)
        
