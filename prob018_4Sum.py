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
        res = []
        self.nsum(nums, target, 4, [], res)
        return res
        
    def nsum(self, nums, target, n, tmp, res):
        if len(nums) < n:
            return
        if n == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(tmp + [nums[l], nums[r]])
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
            for i in range(len(nums) - n + 1):
                if target < nums[i] * n or target > nums[-1] * n:
                    break
                if i == 0 or nums[i] > nums[i-1]:
                    self.nsum(nums[i+1:], target - nums[i], n - 1,
                              tmp + [nums[i]], res)


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
            for tmp_key in three_keys:
                tmp_key.insert(0, nums[i])
                if tmp_key not in keys:
                    keys.append(tmp_key)
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
                    tmp_key = [nums[i], nums[start], nums[end]]
                    if tmp_key not in three_keys:
                        three_keys.append(tmp_key)
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
        res = []
        nums.sort()
        for i in xrange(len(nums)-3):
            newTarget = target - nums[i]
            threeKeys = self.threeSum2(nums[i+1:], newTarget)
            for tmp in threeKeys:
                tmp.insert(0, nums[i])
                if tmp not in res:
                    res.append(tmp)
        return res
        
    def threeSum2(self, nums, target):
        res = []
        for i in xrange(len(nums)-2):
            newTarget = target - nums[i]
            twoKeys = self.twoSum(nums[i+1:], newTarget)
            for tmp in twoKeys:
                tmp.insert(0, nums[i])
                if tmp not in res:
                    res.append(tmp)
        return res
        
    def twoSum(self, nums, target):
        res = []
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                tmp = [dic[n], n]
                if tmp not in res:
                    res.append(tmp)
            else:
                dic[target-n] = n
        return res
