"""
Problem 1 from leetcode: Two Sum.

Given an array of integers, find two numbers such that 
they add up to a specific target number.

The function twoSum should return indices of the two numbers 
such that they add up to the target, where index1 must be less 
than index2. Please note that your returned answers (both index1 
and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sort nums
        temp = sorted(nums)

        index1 = 0
        index2 = 1
        if temp[index1] + temp[index2] > target:
            index1 = 0
            index2 = 0
            print("No solution exist!")
            return [index1, index2]
        for index1 in range(0,(len(temp)-1)):
            for index2 in range((index1+1),len(temp)):
                if temp[index1] + temp[index2] < target:
                    continue
                elif temp[index1] + temp[index2] == target:
                    index1 = nums.index(temp[index1]) + 1
                    index2 = nums.index(temp[index2]) + 1
                    # Equal value case
                    if index1 == index2:
                        index2 = nums.index(temp[index2], index1) + 1
                    return [min(index1, index2), max(index1, index2)]
                elif temp[index1] + temp[index2] > target:
                    break
        print("No solution found!")
        index1 = 0
        index2 = 0
        return [index1, index2]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if d.has_key(n):
                return [d[n]+1, i+1]
            else:
                d[target-n] = i
        return [0, 0]
