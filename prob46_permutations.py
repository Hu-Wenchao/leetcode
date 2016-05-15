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
        ret = [[]]
        for num in nums:
            new_ret = []
            for seq in ret:
                for i in xrange(len(seq) + 1):
                    new_ret.append(seq[:i] + [num] + seq[i:])
            ret = new_ret
        return ret
        
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
            
                
            
        

