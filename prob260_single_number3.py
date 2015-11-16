"""
Given an array of numbers nums, in which exactly 
two elements appear only once and all the other 
elements appear exactly twice. Find the two 
elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So 
in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime 
complexity. Could you implement it using only 
constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        result = []
        for (k, v) in nums_dict.iteritems():
            if v == 1:
                result.append(k)
        return result

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] != nums[i+1]:
                result.append(nums[i])
                i += 1
            else:
                i += 2
        if len(result) == 1:
            result.append(nums[-1])
        elif len(result) == 0:
            return nums[-2:]
        return result
