"""
Given an array S of n integers, are there elements a, b, c, and d 
in S such that a + b + c + d = target? Find all unique quadruplets 
in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in 
non-descending order.

The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        keys = []
        if len(nums) < 4:
            return keys
        nums.sort()
        for i in range(0, len(nums)-3):
            new_target = target - nums[i]
            three_keys = self.threeSum(nums[i+1:len(nums)], new_target)
            for temp_key in three_keys:
                temp_key.insert(0, nums[i])
                if temp_key not in keys:
                    keys.append(temp_key)
        return keys
    
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        three_keys = []
        for i in range(0, len(nums)-2):
            new_target = target - nums[i]
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                if nums[start] + nums[end] == new_target:
                    temp_key = [nums[i], nums[start], nums[end]]
                    if temp_key not in three_keys:
                        three_keys.append(temp_key)
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < new_target:
                    start += 1
                else:
                    end -= 1
        return three_keys
        
