"""
Say you have an array for which the ith element is the 
price of a given stock on day i.

Design an algorithm to find the maximum profit. You may 
complete at most k transactions.
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) 
                       if i - j > 0)
        globalMax = [[0] * n for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            localMax = [0] * n
            for j in xrange(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(
                    globalMax[i - 1][j - 1] + profit,
                    globalMax[i - 1][j - 1],
                    localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]
