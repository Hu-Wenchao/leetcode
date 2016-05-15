"""
Given a collection of candidate numbers (C) and
 a target number (T), find all unique combinations
 in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in
 non-descending order. (ie, a1 <= a2 <= … <= ak).

The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 

A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []
        self.rec(candidates, target, 0, 0, [], ret)
        return ret

    def rec(self, candidates, target, idx, tmpsum, tmplist, ret):
        if tmpsum == target and tmplist not in ret:
            ret.append(list(tmplist))
        for i in xrange(idx, len(candidates)):
            if tmpsum + candidates[i] > target:
                break
            tmplist.append(candidates[i])
            self.rec(candidates, target, i+1,
                     tmpsum+candidates[i], tmplist, ret)
            tmplist.pop()
