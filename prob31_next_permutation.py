"""
Implement next permutation, which rearranges numbers 
into the lexicographically next greater permutation 
of numbers.

If such arrangement is not possible, it must rearrange 
it as the lowest possible order (ie, sorted in ascending 
order).

The replacement must be in-place, do not allocate 
extra memory.

Here are some examples. Inputs are in the left-hand 
column and its corresponding outputs are in the 
right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        ide = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                ide = i - 1
                break
        if ide != -1:
            for i in range(n-1, ide, -1):
                if nums[i] > nums[ide]:
                    nums[i], nums[ide] = nums[ide], nums[i]
                    break
            left = ide + 1
            right = n-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            nums = nums.reverse()
        return
        
