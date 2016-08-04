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
        buy1 = float('inf')
        buy2 = -float('inf')
        profit1 = 0
        profit2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = max(buy2, profit1 - price)
            profit2 = max(profit2, price + buy2)
        return profit2
