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
        curstr = "1"
        curposi = 1
        while curposi < n:
            curstr = self.nextStr(curstr)
            curposi += 1
        return curstr

    def nextStr(self, curstr):
        pre_c = curstr[0]
        next_str = [1, pre_c]
        alter = 1
        for i in range(1, len(curstr)):
            cur_c = curstr[i]
            if cur_c == pre_c:
                next_str[2*alter - 2] += 1
            else:
                pre_c = cur_c
                next_str.append(1)
                next_str.append(pre_c)
                alter += 1
        temp_str = ""
        for item in next_str:
            temp_str += str(item)
        return temp_str
                
