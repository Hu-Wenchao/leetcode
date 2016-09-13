"""
Given two integers n and k, return all possible
combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in xrange(1, n+1)]
        elif k == n:
            return [[i for i in xrange(1, n+1)]]
        else:
            res = self.combine(n-1, k)
            part = self.combine(n-1, k-1)
            for tmp in part:
                tmp.append(n)
            res += part
            return res
