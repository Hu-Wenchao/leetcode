"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = [[]]
        for n in nums:
            tmp = []
            for seq in res:
                for i in xrange(len(seq), -1, -1):
                    if i < len(seq) and seq[i] == n:
                        break
                    tmp.append(seq[:i] + [n] + seq[i:])
            res = tmp
        return res
