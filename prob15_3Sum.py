"""
Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. 

The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Accepted by leetcode.
        keys = []
        if len(nums) < 3:
            return keys
        nums.sort()
        
        for i in range(0, len(nums)-2):
            if (i == 0 or nums[i] > nums[i-1]):
                negate = -nums[i]
                start = i + 1
                end = len(nums) - 1
                while (start < end):
                    # case 1
                    if nums[start] + nums[end] == negate:
                        temp_key = [nums[i], nums[start], nums[end]]
                        temp_key.sort()
                        keys.append(temp_key)
                        start += 1
                        end -= 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    # case 2
                    elif nums[start] + nums[end] < negate:
                        start += 1
                    else:
                        end -= 1
        return keys
