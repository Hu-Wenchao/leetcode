"""
Given an unsorted array, find the maximum difference 
between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative 
integers and fit in the 32-bit signed integer range.
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or max(nums) == min(nums):
            return 0
        nmax, nmin, nlen = max(nums), min(nums), len(nums)
        bsize = 1.0 * (nmax - nmin) / nlen
        bucket = [[2**31-1, -1] for _ in xrange(nlen + 1)]
        for n in nums:
            index = int((n - nmin) // bsize)
            bucket[index][0] = min(bucket[index][0], n)
            bucket[index][1] = max(bucket[index][1], n)
        res, pre = 0, bucket[0][0]
        for tmp in bucket:
            if tmp != [2**31-1, -1]:
                res = max(res, tmp[0] - pre)
                pre = tmp[1]
        return res

    def maximumGap2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or max(nums) == min(nums):
            return 0
        nums = self.radix(nums)
        res = 0
        for i in xrange(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        return res

    def radix(self, nums):
        for i in xrange(len(str(max(nums)))):
            tmp = [[] for _ in xrange(10)]
            for n in nums:
                tmp[n / (10**i) % 10].append(n)
            nums = [a for b in tmp for a in b]
        return nums
