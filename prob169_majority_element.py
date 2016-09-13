"""
Given an array of size n, find the majority element. 
The majority element is the element that appears 
more than |_ n/2 _| times.

You may assume that the array is non-empty and the 
majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums) / 2)]

    def majorityElement2(self, nums):
        count = 1
        major = nums[0]
        for n in nums[1:]:
            if count == 0:
                major = n
                count = 1
            elif major == n:
                count += 1
            else:
                count -= 1
        return major
