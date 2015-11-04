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
        if len(s) < 2 or numRows == 1:
            return s
            
        temp = 2*numRows - 2
        line = [""] * temp
        
        if len(s) >= temp:
            for i in range(len(s) // temp):
                for j in range(temp):
                    line[j] += s[i*temp + j]
        for i in range(len(s) % temp):
            line[i] += s[(len(s) // temp) * temp + i]

        for i in range(numRows-2):
            line[i+1] = self.mergeRows(line[i+1], line[-i-1])

        newRow = ""
        for i in range(numRows):
            newRow += line[i]
        
        return newRow        

    def mergeRows(self, row1, row2):
        mergedRow = ""
        for i in range(len(row2)):
            mergedRow += row1[i]
            mergedRow += row2[i]
        if len(row1) > len(row2):
            mergedRow += row1[-1]
        return mergedRow
