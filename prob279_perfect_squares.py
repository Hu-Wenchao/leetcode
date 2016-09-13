"""
Given a positive integer n, find the least number of perfect 
square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; 
given n = 13, return 2 because 13 = 4 + 9.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        squares = [i*i for i in xrange(1, 1+int(n**0.5))]
        cnt = 0
        dic = (n)
        while dic:
            cnt += 1
            tmp = set()
            for x in dic:
                for y in squares:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.add(x-y)
            dic = tmp
        return cnt
