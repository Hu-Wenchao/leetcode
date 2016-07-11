"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = [[]]
        for n in nums:
            tmp = []
            for seq in res:
                for i in xrange(len(seq) + 1):
                    tmp.append(seq[:i] + [n] + seq[i:])
            res = tmp
        return res
        
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, seq, res):
        if not nums:
            res.append(seq)
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], seq + [nums[i]], res)
            
            
                
            
        

