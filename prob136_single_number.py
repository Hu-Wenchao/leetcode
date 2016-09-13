"""
Given an array of integers, every element 
appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime 
complexity. Could you implement it without 
using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for n in dic.keys():
            if dic[n] == 1:
                return n
