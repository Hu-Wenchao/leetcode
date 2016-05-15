"""
The string "PAYPALISHIRING" is written in a zigzag
 pattern on a given number of rows like this: (you
 may want to display this pattern in a fixed font
 for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make
 this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step = (numRows == 1) - 1
        tmp = [''] * numRows
        i = 0
        for ch in s:
            tmp[i] += ch
            if i == 0 or i == numRows - 1:
                step = -step
            i += step
        return ''.join(tmp)
