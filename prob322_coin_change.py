"""
You are given coins of different denominations and a total 
amount of money amount. Write a function to compute the 
fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination 
of the coins, return -1.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1

    def coinChange(self, coins, amount):
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        sortedCoins = sorted(coins, reverse=True)
        upperBound = (amount + sortedCoins[-1] - 1) / sortedCoins[-1] + 1
        self.bestNCoins = upperBound
        self.branchAndBoundSearch(sortedCoins, amount, 0)
        if self.bestNCoins == upperBound:
            return -1
        else:
            return self.bestNCoins

    def branchAndBoundSearch(self, sortedCoins, amount, nCoins):
        lowerBound = nCoins + (amount + sortedCoins[0] - 1) / sortedCoins[0]
        if lowerBound > self.bestNCoins:
            return
        if len(sortedCoins) == 0:
            return
        if amount == sortedCoins[0] and nCoins + 1 < self.bestNCoins:
            self.bestNCoins = nCoins + 1
            return
        if amount > sortedCoins[0]:
            self.branchAndBoundSearch(sortedCoins, amount - sortedCoins[0], nCoins + 1)
        if len(sortedCoins) > 1:
            self.branchAndBoundSearch(sortedCoins[1:], amount, nCoins)
