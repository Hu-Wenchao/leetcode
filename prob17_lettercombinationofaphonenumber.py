"""
Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the
telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        solution = [""]
        for i in range(len(digits)):
            templist = []
            for string in solution:
                if digits[i] == "2":
                    templist.append(string + "a")
                    templist.append(string + "b")
                    templist.append(string + "c")
                elif digits[i] == "3":
                    templist.append(string + "d")
                    templist.append(string + "e")
                    templist.append(string + "f")
                elif digits[i] == "4":
                    templist.append(string + "g")
                    templist.append(string + "h")
                    templist.append(string + "i")
                elif digits[i] == "5":
                    templist.append(string + "j")
                    templist.append(string + "k")
                    templist.append(string + "l")
                elif digits[i] == "6":
                    templist.append(string + "m")
                    templist.append(string + "n")
                    templist.append(string + "o")
                elif digits[i] == "7":
                    templist.append(string + "p")
                    templist.append(string + "q")
                    templist.append(string + "r")
                    templist.append(string + "s")
                elif digits[i] == "8":
                    templist.append(string + "t")
                    templist.append(string + "u")
                    templist.append(string + "v")
                elif digits[i] == "9":
                    templist.append(string + "w")
                    templist.append(string + "x")
                    templist.append(string + "y")
                    templist.append(string + "z")
            solution = templist
        return solution
