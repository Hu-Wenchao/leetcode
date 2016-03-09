"""
Given n, how many structurally unique BST's 
(binary search trees) that store values 1...n?
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        
        ret = [0] * (n + 1)
        ret[0] = 1
        ret[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                ret[i] += ret[j] * ret[i-1-j]
        
        return ret[-1]