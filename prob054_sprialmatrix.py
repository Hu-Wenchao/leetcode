"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        rbegin, rend, cbegin, cend = 0, len(matrix)-1, 0, len(matrix[0])-1
        while rbegin <= rend and cbegin <= cend:
            for i in xrange(cbegin, cend+1):
                res.append(matrix[rbegin][i])
            rbegin += 1
            for i in xrange(rbegin, rend+1):
                res.append(matrix[i][cend])
            cend -= 1
            if rbegin <= rend:
                for i in xrange(cend, cbegin-1, -1):
                    res.append(matrix[rend][i])
                rend -= 1
            if cbegin <= cend:
                for i in xrange(rend, rbegin-1, -1):
                    res.append(matrix[i][cbegin])
                cbegin += 1
        return res
