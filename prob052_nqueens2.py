"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, 
return the total number of distinct solutions.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        self.dfs(n, [], [], [], result)
        return len(result)

    def dfs(self, n, queens, xy_dif, xy_sum, result):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in xrange(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                self.dfs(n, queens+[q], xy_dif+[p-q], xy_sum+[p+q], result)
