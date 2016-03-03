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
        o1 = max(prices) * 100
        o2 = -o1
        for i in range(len(prices)):
            o1 = min(o1, prices[i])
            profit1 = max(profit1, prices[i] - o1)
            o2 = max(o2, profit1-prices[i])
            profit2 = max(profit2, prices[i]+o2)
        return profit2
