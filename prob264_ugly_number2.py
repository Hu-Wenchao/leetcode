"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors 
only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 
9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        n2 = 0
        n3 = 0
        n5 = 0
        while len(ugly) < n:
            u2 = ugly[n2] * 2
            u3 = ugly[n3] * 3
            u5 = ugly[n5] * 5
            u = min(u2, u3, u5)
            if u == u2:
                n2 += 1
            if u == u3:
                n3 += 1
            if u == u5:
                n5 += 1
            ugly += u,
            # ugly.append(u)
        return ugly[-1]
