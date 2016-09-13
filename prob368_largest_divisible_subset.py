"""
Given a set of distinct positive integers, find the largest 
subset such that every pair (Si, Sj) of elements in this subset 
satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        cont = [1] * len(nums)
        par = [-1] * len(nums)
        m, mi = 0, 1
        for i in xrange(len(nums)):
            for j in xrange(i):
                if not nums[i] % nums[j] and cont[i] <= cont[j]:
                    cont[i] = cont[j] + 1
                    par[i] = j
            if cont[i] > m:
                m, mi = cont[i], i
        res = []
        while mi >= 0:
            res.append(nums[mi])
            mi = par[mi]
        return res
