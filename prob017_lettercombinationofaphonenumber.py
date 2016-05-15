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
        ph = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        ret = list(ph[digits[0]])
        for d in digits[1:]:
            tmp = []
            for ch in ph[d]:
                tmp += [term + ch for term in ret]
            ret = tmp
        return ret
