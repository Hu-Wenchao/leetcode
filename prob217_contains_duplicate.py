"""
Given an array of integers, find if the array contains 
any duplicates. Your function should return true if any 
value appears at least twice in the array, and it should 
return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return True
        return False

