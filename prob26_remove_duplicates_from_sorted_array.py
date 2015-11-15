"""
Given a sorted array, remove the duplicates in place such 
that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do 
this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two 
elements of nums being 1 and 2 respectively. It doesn't matter 
what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        pre_c = nums[0]
        list_length = 1
        i = 1
        while i < len(nums):
            cur_c = nums[i]
            if cur_c == pre_c:
                nums.remove(cur_c)
            else:
                pre_c = cur_c
                list_length += 1 
                i += 1
        return list_length
