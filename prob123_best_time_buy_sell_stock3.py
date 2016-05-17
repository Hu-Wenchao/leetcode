"""
Say you have an array for which the ith element is 
the price of a given stock on day i.

Design an algorithm to find the maximum profit. Y
ou may complete at most two transactions.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit1 = 0
        profit2 = 0
        buy1 = float('inf')
        buy2 = -float('inf')
        for i in xrange(len(prices)):
            buy1 = min(buy1, prices[i])
            profit1 = max(profit1, prices[i] - buy1)
            buy2 = max(buy2, profit1 - prices[i])
            profit2 = max(profit2, prices[i] + buy2)
        return profit2
