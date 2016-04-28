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
        ret = '1'
        while n > 1:
            ret = self.nextStr(ret)
            n -= 1
        return ret

    def nextStr(self, s):
        ret = ''
        prechar = s[0]
        tmp = 1
        for c in s[1:]:
            if c == prechar:
                tmp += 1
            elif c != prechar:
                ret += str(tmp) + prechar
                prechar = c
                tmp = 1
        ret += str(tmp) + prechar
        return ret
                
