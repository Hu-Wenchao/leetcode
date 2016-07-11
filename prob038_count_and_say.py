"""
The count-and-say sequence is the sequence of integers
beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        while n > 1:
            res = self.nextStr(res)
            n -= 1
        return res

    def nextStr(self, s):
        res = ''
        pre = s[0]
        num = 1
        for c in s[1:]:
            if c == pre:
                num += 1
            else:
                res += str(num) + pre
                pre = c
                num = 1
        res += str(num) + pre
        return res
                
