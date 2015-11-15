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
        nums = ["M", "D", "C", "L", "X", "V", "I"]
        ints = [1000, 500, 100, 50, 10, 5, 1]
        for c in s:
            if not c in nums:
                raise ValueError, "nums is not a valid roman numeral"
        places = []
        for i in range(len(s)):
            c = s[i]
            value = ints[nums.index(c)]
            # if the next place holds a larger number, this value is negative.
            try:
                nextvalue = ints[nums.index(s[i+1])]
                if nextvalue > value:
                    value *= -1
            except IndexError:
                # there is no next place.
                pass
            places.append(value)
        sum = 0
        for n in places:
            sum += n
        return sum

    def romanToInt2(self, s):
        #Define digit mapping
        romanNumeralMap = (('M',  1000),
                           ('CM', 900),
                           ('D',  500),
                           ('CD', 400),
                           ('C',  100),
                           ('XC', 90),
                           ('L',  50),
                           ('XL', 40),
                           ('X',  10),
                           ('IX', 9),
                           ('V',  5),
                           ('IV', 4),
                           ('I',  1))
        result = 0
        index = 0
        for numeral, integer in romanNumeralMap:
            while s[index:index+len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result
        
