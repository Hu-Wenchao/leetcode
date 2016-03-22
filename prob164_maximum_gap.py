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
        if len(nums) < 2 or max(nums)-min(nums) == 0:   # in case bsize == 0
            return 0
        maxn,minn,lenn = max(nums),min(nums),len(nums)
        bsize = (maxn - minn + 1.0) / lenn  # could have interger issue on OJ
        buckets = [[2**31-1, -1] for _ in range(lenn+1)]
        for i in nums:
            place = int( (i-minn) // bsize )
            buckets[place][0] = min(i, buckets[place][0])
            buckets[place][1] = max(i, buckets[place][1])
        res, prev = 0, buckets[0][0]
        for i in buckets:
            if i != [2**31-1, -1]:
                res = max(res, i[0]-prev)
                prev = i[1]
        return res

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = self.radixSort(nums)
        ans = 0
        if len(A) == 0: return 0
        prev = A[0]
        for i in A:
            if i - prev > ans: 
                ans = i - prev
            prev = i
        return ans

    def radixSort(self, A): 
        for k in xrange(10):     
            s=[[] for i in xrange(10)]
            for i in A:
                s[i/(10**k)%10].append(i)
            A=[a for b in s for a in b] 
        return A
