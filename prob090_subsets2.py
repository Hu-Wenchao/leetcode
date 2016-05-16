"""
Given a collection of integers that might contain 
duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for n in nums:
            for tmp in [x + [n] for x in res]:
                if tmp not in res:
                    res.append(tmp)
        return res
