"""
There are N children standing in a line. 
Each child is assigned a rating value.

You are giving candies to these children 
subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        qty = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                qty[i] = qty[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                qty[i-1] = max(qty[i-1], qty[i] + 1)
        return sum(qty)
