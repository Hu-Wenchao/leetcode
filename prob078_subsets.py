"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            for i in xrange(len(res)):
                res.append(res[i] + [n])
        return res

    def subsets2(self, nums):
        # Lets assign bits to each outcome  -> First bit to 1 ,
        # Second bit to 2 and third bit to 3
        # Take = 1
        # Dont take = 0

        # 0) 0 0 0  -> Dont take 3, Dont take 2, Dont take 1 = { } 
        # 1) 0 0 1  -> Dont take 3, Dont take 2, take 1 =  {1 } 
        # 2) 0 1 0  -> Dont take 3, take 2, Dont take 1 = { 2 } 
        # 3) 0 1 1  -> Dont take 3, take 2, take 1 = { 1 , 2 } 
        # 4) 1 0 0  -> take 3, Dont take 2, Dont take 1 = { 3 } 
        # 5) 1 0 1  -> take 3, Dont take 2, take 1 = { 1 , 3 } 
        # 6) 1 1 0  -> take 3, take 2, Dont take 1 = { 2 , 3 } 
        # 7) 1 1 1  -> take 3, take 2, take 1 = { 1 , 2 , 3 }
        nums.sort()
        total = 2**len(nums)
        res = [[] for _ in xrange(total)]
        for i in xrange(len(nums)):
            for j in xrange(total):
                if ((j>>i)&1) > 0:
                    res[j].append(nums[i])
        return res
