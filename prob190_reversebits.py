"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented 
in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 
00111001011110000010100101000000).
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
    
    def reverseBits2(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(format(n, '#034b')[:1:-1],2)
