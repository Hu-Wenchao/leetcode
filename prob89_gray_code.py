"""
The gray code is a binary numeral system where 
two successive values differ in only one bit.

Given a non-negative integer n representing 
the total number of bits in the code, 
print the sequence of gray code. 
A gray code sequence must begin with 0.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(n):
            ret += [x + 2**i for x in reversed(ret)]
        return ret
