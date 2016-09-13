"""
Given a sorted positive integer array nums and an integer n, 
add/patch elements to the array such that any number in 
range [1, n] inclusive can be formed by the sum of some 
elements in the array. Return the minimum number of 
patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form 
possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: 
[1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers 
the range [1, 6].
So we only need 1 patch.
"""

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        patch = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patch += 1
        return patch
