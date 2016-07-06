"""
Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. 

The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                target = -nums[i]
                b, e = i + 1, len(nums) - 1
                while b < e:
                    if nums[b] + nums[e] == target:
                        res.append([nums[i], nums[b], nums[e]])
                        b += 1
                        e -= 1
                        while b < e and nums[b] == nums[b-1]:
                            b += 1
                        while b < e and nums[e] == nums[e+1]:
                            e -= 1
                    elif nums[b] + nums[e] < target:
                        b += 1
                    else:
                        e -= 1
        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                target = -nums[i]
                tmp = self.twoSum(nums[i+1:], target)
                for term in tmp:
                    if term not in res:
                        res.append(term)
        return res
        
    def twoSum(self, nums, target):
        d = {}
        res = []
        for i, num in enumerate(nums):
            if num in d:
                tmp = [-target, d[num], num]
                if tmp not in res:
                    res.append(tmp)
            else:
                d[target-num] = num
        return res
