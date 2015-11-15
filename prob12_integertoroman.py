"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sol = []
        sol.append(self.digitToRoman(num/1000, " ", " ", "M"))
        sol.append(self.digitToRoman((num/100)%10, "M", "D", "C"))
        sol.append(self.digitToRoman((num/10)%10, "C", "L", "X"))
        sol.append(self.digitToRoman(num%10, "X", "V", "I"))
        return "".join(sol)

    def digitToRoman(self, num, charTen, charFive, charOne):
        char = []
        if num > 8:
            for i in range(num, 10):
                char.append(charOne)
            char.append(charTen)
        elif num >= 5:
            char.append(charFive)
            for i in range(5, num):
                char.append(charOne)
        elif num > 3:
            for i in range(num, 5):
                char.append(charOne)
            char.append(charFive)
        else:
            for i in range(0, num):
                char.append(charOne)
        return "".join(char)

    def intToRoman2(self, num):
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                "V", "IV", "I")
        result = ""
        for i in range(len(ints)):
            count = int(num / ints[i])
            result += nums[i] * count
            num -= ints[i] * count
        return result

    def intToRoman3(self, num):
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
        result = ""
        while numeral, integer in romanNumeralMap:
            while num >= integer:
                result += numeral
                num -= integer
        return result
