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
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        res = []
        for (k, v) in dic.iteritems():
            if v == 1:
                res.append(k)
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] != nums[i+1]:
                res.append(nums[i])
                i += 1
            else:
                i += 2
        if len(res) == 1:
            res.append(nums[-1])
        elif len(res) == 0:
            return nums[-2:]
        return res
