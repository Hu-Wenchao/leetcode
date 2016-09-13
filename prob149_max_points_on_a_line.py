"""
Given n points on a 2D plane, find the maximum number of 
points that lie on the same straight line.
"""

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            same = 0
            x0, y0 = points[i].x, points[i].y
            dic = {x0 : 1}
            for j in range(i+1, len(points)):
                x1, y1 = points[j].x, points[j].y
                if x1 == x0 and y1 == y0:
                    same += 1
                    continue
                if x1 == x0:
                    slope = x0
                else:
                    slope = 1.0 * (y1 - y0) / (x1 - x0)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            res = max(res, max(dic.values()) + same)
        return res
