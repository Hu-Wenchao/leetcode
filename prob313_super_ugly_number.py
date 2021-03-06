"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime 
factors are in the given prime list primes of size k. For 
example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the 
sequence of the first 12 super ugly numbers given 
primes = [2, 7, 13, 19] of size 4.
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        q, ugly = [], [1]
        for i in xrange(len(primes)):
            heapq.heappush(q, (primes[i], 0, primes[i]))
        while len(ugly) < n:
            x, i, p = q[0]
            ugly.append(x)
            while q and q[0][0] == x:
                x, i, p = heapq.heappop(q)
                heapq.heappush(q, (p * ugly[i+1], i+1, p))
        return ugly[-1]
