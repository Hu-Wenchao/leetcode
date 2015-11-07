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
        candidates = list(range(1, n+1))
        solution = []
        self.combineRec(candidates, k, 0, [], solution)
        return solution

    def combineRec(self, candidates, k, index, templist, solution):
        if len(templist) == k and templist not in solution:
            solution.append(list(templist))
            return
        for i in range(index, len(candidates)):
            if len(templist) < k:
                templist.append(candidates[i])
                self.combineRec(candidates, k, i+1, templist, solution)
            templist.pop()
