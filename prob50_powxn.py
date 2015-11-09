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
        # not accepted by leetcode because of time limit
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        
        if n < 0:
            return 1.0 / self.myPow2(x, -n)
        else:
            return self.myPow2(x, n/2) * self.myPow2(x, n - n/2)

    def myPow3(self, x, n):
        # bit operation
        if n == 0:
            return 1
        
        if n < 0:
            return 1.0 / self.myPow3(x, -n)
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            n = n / 2
            x = x * x
        return result
            
