"""
Given a sorted integer array without duplicates, return 
the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        s = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i-1] != s:
                    res.append(str(s) + '->' + str(nums[i-1]))
                else:
                    res.append(str(s))
                s = nums[i]
        if nums[-1] != s:
            res.append(str(s) + '->' + str(nums[-1]))
        else:
            res.append(str(s))
        return res
