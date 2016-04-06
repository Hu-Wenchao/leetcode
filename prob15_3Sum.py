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
        if len(nums) < 3:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                negate = -nums[i]
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] == negate:
                        ret.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif nums[start] + nums[end] < negate:
                        start += 1
                    else:
                        end -= 1
        return ret

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                target = -nums[i]
                temp = self.twoSum(nums[i+1:], target)
                for term in temp:
                    if term not in ret:
                        ret.append(term)
        return ret
        
    def twoSum(self, nums, target):
        d = {}
        ret = []
        for i, num in enumerate(nums):
            if num in d:
                temp = [-target, d[num], num]
                if temp not in ret:
                    ret.append(temp)
            else:
                d[target-num] = num
        return ret
