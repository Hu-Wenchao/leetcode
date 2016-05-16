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
        ret = []
        if not matrix:
            return ret
        rbegin, rend, cbegin, cend = 0, len(matrix)-1, 0, len(matrix[0])-1

        while rbegin <= rend and cbegin <= cend:
            for j in xrange(cbegin, cend+1):
                ret.append(matrix[rbegin][j])
            rbegin += 1

            for j in xrange(rbegin, rend+1):
                ret.append(matrix[j][cend])
            cend -= 1

            if rbegin <= rend:
                for j in xrange(cend, cbegin-1, -1):
                    ret.append(matrix[rend][j])
            rend -= 1

            if cbegin <= cend:
                for j in xrange(rend, rbegin-1, -1):
                    ret.append(matrix[j][cbegin])
            cbegin += 1

        return ret
