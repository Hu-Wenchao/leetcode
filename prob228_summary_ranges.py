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
        ret = []
        if not nums:
            return ret
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - end == 1:
                end += 1
            else:
                if start != end:
                    ret.append(str(start) + '->' + str(end))
                else:
                    ret.append(str(start))        
                start = nums[i]
                end = nums[i]
        if start != end:
            ret.append(str(start) + '->' + str(end))
        else:
            ret.append(str(start))
        return ret
