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
