"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        nums = list(range(1, n + 1))
        res = ''
        k -= 1
        while n > 0:
            n -= 1
            i, k = divmod(k, factorial(n))
            res += str(nums[i])
            nums.remove(nums[i])
        return res
