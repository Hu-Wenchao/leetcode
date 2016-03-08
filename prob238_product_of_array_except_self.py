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
        forward_product = [0] * len(nums)
        backward_product = [0] * len(nums)
        forward_product[0] = nums[0]
        backward_product[-1] = nums[-1]
        for i in range(1, len(nums)-1):
            forward_product[i] = forward_product[i-1] * nums[i] 
            backward_product[-i-1] = backward_product[-i] * nums[-i-1]
        forward_product[-1] = forward_product[-2] * nums[-1]
        backward_product[0] = backward_product[1] * nums[0]
        
        ret = [0] * len(nums)
        ret[0] = backward_product[1]
        ret[-1] = forward_product[-2]
        for i in range(1, len(nums)-1):
            ret[i] = forward_product[i-1] * backward_product[i+1]

        return ret
