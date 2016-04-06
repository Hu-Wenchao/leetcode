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
    # Solution 1
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.nSum(nums, target, 4, [], results)
        return results

    def nSum(self, nums, target, n, result, results):
        if len(nums) < n or n < 2:
            return
        if n == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-n+1):
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    self.nSum(nums[i+1:], target-nums[i], n-1,
                              result+[nums[i]], results)


    # Solution 2
    def fourSum2(self, nums, target):
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
        
    # Solution 3
    def fourSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        ret = []
        nums.sort()
        for i in xrange(len(nums)-3):
            newTarget = target - nums[i]
            threeKeys = self.threeSum2(nums[i+1:], newTarget)
            for temp in threeKeys:
                temp.insert(0, nums[i])
                if temp not in ret:
                    ret.append(temp)
        return ret
        
    def threeSum2(self, nums, target):
        ret = []
        for i in xrange(len(nums)-2):
            newTarget = target - nums[i]
            twoKeys = self.twoSum(nums[i+1:], newTarget)
            for temp in twoKeys:
                temp.insert(0, nums[i])
                if temp not in ret:
                    ret.append(temp)
        return ret
        
    def twoSum(self, nums, target):
        ret = []
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                temp = [d[num], num]
                if temp not in ret:
                    ret.append(temp)
            else:
                d[target-num] = num
        return ret
