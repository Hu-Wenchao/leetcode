"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        result = 0
        for i in xrange(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result + roman[s[-1]]

    def romanToInt2(self, s):
        roman = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), 
                 ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), 
                 ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        result = 0
        id = 0
        for r, n in roman:
            while s[id : id+len(r)] == r:
                result += n
                id += len(r)
        return result
