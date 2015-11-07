"""
Find all possible combinations of k numbers that
 add up to a number n, given that only numbers
 from 1 to 9 can be used and each combination
 should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = list(range(1,10))
        solution = []
        self.combinationSum3Rec(candidates, n, k, 0, 0, [], solution)
        return solution

    def combinationSum3Rec(self, candidates, n, k, index, tempsum, templist,
                           solution):
        if tempsum == n and len(templist) == 3:
            solution.append(list(templist))
            return
        for i in range(index, len(candidates)):
            if tempsum + candidates[i] > n or len(templist) > k:
                break
            templist.append(candidates[i])
            self.combinationSum3Rec(candidates, n, k, i+1,
                                    tempsum+candidates[i],
                                    templist, solution)
            templist.pop()
