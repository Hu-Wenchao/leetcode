"""
Given an array of n integers where n > 1, nums, 
return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        forward = [0] * len(nums)
        backward = [0] * len(nums)
        forward[0] = nums[0]
        backward[-1] = nums[-1]
        for i in range(1, len(nums)-1):
            forward[i] = forward[i-1] * nums[i] 
            backward[-i-1] = backward[-i] * nums[-i-1]
        forward[-1] = forward[-2] * nums[-1]
        backward[0] = backward[1] * nums[0]      
        res = [0] * len(nums)
        res[0] = backward[1]
        res[-1] = forward[-2]
        for i in range(1, len(nums)-1):
            res[i] = forward[i-1] * backward[i+1]
        return res
