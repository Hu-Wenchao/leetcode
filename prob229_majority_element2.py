"""
Given an integer array of size n, find all elements that appear 
more than ⌊ n/3 ⌋ times. The algorithm should run in linear time 
and in O(1) space.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        cnt1, cnt2, n1, n2 = 0, 0, 0, 1
        for n in nums:
            if n == n1:
                cnt1 += 1
            elif n == n2:
                cnt2 += 1
            elif cnt1 == 0:
                n1, cnt1 = n, 1
            elif cnt2 == 0:
                n2, cnt2 = n, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        return [n for n in (n1, n2) if nums.count(n) > len(nums) // 3]
            
