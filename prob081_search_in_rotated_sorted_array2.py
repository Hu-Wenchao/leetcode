"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) / 2
            if nums[m] == target:
                return True
            # skip duplicates
            while l < m and nums[l] == nums[m]:
                l += 1
            # the first half is ordered
            if nums[l] <= nums[m]:
                # target is in the first half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
