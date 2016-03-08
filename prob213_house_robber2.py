"""
After robbing those houses on that street, the thief 
has found himself a new place for his thievery so 
that he will not get too much attention. This time, 
all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the 
last one. Meanwhile, the security system for these 
houses remain the same as for those in the previous 
street.

Given a list of non-negative integers representing 
the amount of money of each house, determine the 
maximum amount of money you can rob tonight without 
alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
            
        return max(self.robrow(nums[1:]), self.robrow(nums[:-1]))

    def robrow(self, row):
        a = 0
        b = 0
        for i in range(len(row)):
            if i % 2 == 0:
                a = max(a + row[i], b)
            else:
                b = max(b + row[i], a)
        return max(a, b)

        
