"""
Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n, 0, 0, '', res)
        return res

    def generate(self, n, l, r, tmp, res):
        if r == n:
            res.append(tmp)
            return
        if l < n:
            self.generate(n, l+1, r, tmp + '(', res)
        if r < l:
            self.generate(n, l, r+1, tmp + ')', res)
