"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda interval:interval.start)
        if len(intervals) <= 1:
            return intervals
        interval = intervals[0]
        ret = []
        for i in range(1, len(intervals)):
            interval2 = intervals[i]
            if interval.end < interval2.start:
                ret.append(interval)
                interval = interval2
            else:
                interval.end = max(interval.end, interval2.end)
        ret.append(interval)
        return ret
