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
        solution = []
        # both solutions are correct
        self.combinationSum2Rec(candidates, target, 0, 0, [], solution)
        # self.combinationSum2Rec2(candidates, target, 0, 0, [], solution)
        return solution

    def combinationSum2Rec(self, candidates, target, index, tempsum,
                           templist, solution):
        if tempsum == target and templist not in solutoin:
            solution.append(list(templist))
        for i in range(index, len(candidates)):
            if tempsum + candidates[i] > target:
                break
            templist.append(candidates[i])
            self.combinationSum2Rec(candidates, target, i+1, 
                                    tempsum+candidates[i],
                                    templist, solution)
            templist.pop()
        
    def combinationSum2Rec2(self, candidates, target, index, tempsum,
                            templist, solution):
        if tempsum == target:
            solution.append(list(templist))
            return
        for i in range(index, len(candidates)):
            if (i==index or candidates[i-1]!=candidates[i]) and \
               tempsum + candidates[i] <= target:
                templist.append(candidates[i])
                self.combinationSum2Rec2(candidates, target, i+1,
                                         tempsum+candidates[i],
                                         templist, solution)
                templist.pop()
