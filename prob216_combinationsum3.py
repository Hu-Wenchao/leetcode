"""
Find all possible combinations of k numbers that
 add up to a number n, given that only numbers
 from 1 to 9 can be used and each combination
 should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(xrange(1, 10))
        res = []
        self.rec(nums, n, k, 0, 0, [], res)
        return res

    def rec(self, nums, n, k, index, tmpsum, tmplist, res):
        if tmpsum == n and len(tmplist) == k:
            res.append(list(tmplist))
            return
        for i in xrange(index, len(nums)):
            if tmpsum + nums[i] > n or len(tmplist) > k:
                break
            tmplist.append(nums[i])
            self.rec(nums, n, k, i+1, tmpsum+nums[i], tmplist, res)
            tmplist.pop()
