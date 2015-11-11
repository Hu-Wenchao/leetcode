"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below
and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified
vaguely (ie, no given input specs). You are responsible
to gather all the input requirements up front.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        pointer = 0
        isNegative = False
        if not str:
            return 0
        while pointer < len(str) and str[pointer] == " ":
            pointer += 1
        if pointer == len(str):
            return 0
        if str[pointer] == "-":
            isNegative = True
            pointer += 1
        elif str[pointer] == "+":
            isNegative = False
            pointer += 1
        solution = 0
        for pointer in range(pointer, len(str)):
            if not str[pointer].isdigit():
                break
            else:
                solution = 10 * solution + int(str[pointer])

        if not isNegative and solution > 2147483647:
            return 2147483647
        elif isNegative and solution > 2147483648:
            return -2147483648
        
        if isNegative:
            return -1 * solution
        else:
            return solution
