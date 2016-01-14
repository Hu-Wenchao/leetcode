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
        return int(format(n, '#034b')[:1:-1],2)
