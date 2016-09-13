"""
Implement pow(x, n).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0       
        if n < 0:
            return 1.0 / self.myPow(x, -n)       
        if n % 2 == 1:
            return self.myPow(x * x, n/2) * x
        else:
            return self.myPow(x * x, n/2)

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow2(x, -n)
        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res *= x
            n = n / 2
            x = x * x
        return res
