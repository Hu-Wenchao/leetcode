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
        m = 0
        for i in range(len(points)):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, len(points)):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if points[i].x == tx:
                    slope = 'i'
                else:
                    slope = (points[i].y - ty) * 1.0 / (points[i].x - tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m
            
