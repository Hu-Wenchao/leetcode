"""
Given an integer n, generate a square matrix filled
with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        # this one is the first edition, it is correct but ugly
        # see better version on the bottom
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in xrange(n)]
        rbegin, rend, cbegin, cend = 0, n-1, 0, n-1
        tmp = 1
        while rbegin <= rend and cbegin <= cend:
            for i in xrange(cbegin, cend+1):
                matrix[rbegin][i] = tmp
                tmp += 1
            rbegin += 1
            for i in xrange(rbegin, rend+1):
                matrix[i][cend] = tmp
                tmp += 1
            cend -= 1
            if rbegin <= rend:
                for i in xrange(cend, cbegin-1, -1):
                    matrix[rend][i] = tmp
                    tmp += 1
            rend -= 1
            if cbegin <= cend:
                for i in xrange(rend, rbegin-1, -1):
                    matrix[i][cbegin] = tmp
                    tmp += 1
            cbegin += 1
        return matrix
                    
