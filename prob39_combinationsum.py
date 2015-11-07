"""
Given a set of candidate numbers (C) and a target number (T),
 find all unique combinations in C where the candidate
 numbers sums to T.

The same repeated number may be chosen from C unlimited
 number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ..., ak) must be in
non-descending order. (ie, a1 <= a2 <= ... <= ak).

The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 

A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        solution = []
        self.combinationSumRec(candidates, target, 0, 0, [], solution)
        return solution

    def combinationSumRec(self, candidates, target, index, tempsum,
                          templist, solution):
        if tempsum == target:
            solution.append(list(templist))
        for i in range(index, len(candidates)):
            if tempsum + candidates[i] > target:
                break
            templist.append(candidates[i])
            self.combinationSumRec(candidates, target, i, tempsum+candidates[i],
                                   templist, solution)
            templist.pop()
