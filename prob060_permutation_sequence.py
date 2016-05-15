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

from math import factorial
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in xrange(1, n+1)]

        while n - 1 >= 0:
            num, k = k / factorial(n - 1), k % factorial(n - 1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
                
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])
            
            n -= 1
        
        return ''.join(res)
