"""
There are N gas stations along a circular route, where 
the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs 
cost[i] of gas to travel from station i to its next 
station (i+1). You begin the journey with an empty 
tank at one of the gas stations.

Return the starting gas station's index if you can 
travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        total = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        if total + tank < 0:
            start = -1
        return start

    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        total = gas[start] - cost[start]
        while end < start:
            if total < 0:
                start -= 1
                total += gas[start] - cost[start]
            if total >= 0:
                total += gas[end] - cost[end]
                end += 1
        return start if total >= 0 else -1
            
