"""
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent 
the color red, white, and blue respectively.
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                start += 1
            elif nums[i] == 2:
                end -= 1
                
        nums[0:start] = [0] * start
        nums[start:end] = [1] * (end - start)
        nums[end:] = [2] * (len(nums) - end)

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = [0] * 3
        for num in nums:
            temp[num] += 1
        nums[:temp[0]] = [0] * temp[0]
        nums[temp[0]:temp[0]+temp[1]] = [1] * temp[1]
        nums[temp[0]+temp[1]:temp[0]+temp[1]+temp[2]] = [2] * temp[2]
        return

    def sortColors3(self, nums):
        #[0,i)[i,j)[j,k) are 0s, 1s, 2s
        i = 0
        j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
    
