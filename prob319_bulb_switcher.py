"""
There are n bulbs that are initially off. You first turn on 
all the bulbs. Then, you turn off every second bulb. On the 
third round, you toggle every third bulb (turning on if it's 
off or turning off if it's on). For the ith round, you 
toggle every i bulb. For the nth round, you only toggle 
the last bulb. Find how many bulbs are on after n rounds.
"""

from math import sqrt
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # num = (a ** m) * (b ** n) * ...
        # positive factors number(except 1): f = (m + 1) * (n + 1) - 1
        # if the bulb is on finally, f must be power of another number
        return int(sqrt(n))
