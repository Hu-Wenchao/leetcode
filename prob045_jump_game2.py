"""
Given an array of non-negative integers, you are 
initially positioned at the first index of the array.

Each element in the array represents your maximum 
jump length at that position.

Your goal is to reach the last index in the minimum 
number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index 
is 2. (Jump 1 step from index 0 to 1, then 3 steps to 
the last index.)
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        pre = 0
        cur = 0
        for i in xrange(len(nums)):
            if i > pre:
                pre = cur
                step += 1
            cur = max(cur, i + nums[i])
        return step

    def jump2(self, nums):
        step = 0
        left = 0
        right = 0
        n = len(nums)
        if n == 1:
            return 0
        while left <= right:
            step += 1
            old_right = right
            for i in range(left, old_right+1):
                new_right = i + nums[i]
                if new_right >= n -1:
                    return step
                if new_right > right:
                    right = new_right
            left = old_right + 1
