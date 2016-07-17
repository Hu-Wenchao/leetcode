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
        for i in xrange(len(points)):
            same = 0
            dic = {'i' : 1}
            for j in xrange(i + 1, len(points)):
                x, y = points[j].x, points[j].y
                if x == points[i].x and y == points[i].y:
                    same += 1
                    continue
                if x == points[i].x:
                    slope = i
                else:
                    slope = 1.0 * (points[i].y - y) / (points[i].x - x)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            res = max(res, max(dic.values()) + same)
        return res
