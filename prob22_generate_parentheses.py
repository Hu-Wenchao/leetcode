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
        result = []
        self.generate(n, 0, 0, [], result)
        return result

    def generate(self, n, lp, rp, tmp, result):
        if rp == n:
            result.append(''.join(tmp))
            return
        if lp < n:
            tmp.append('(')
            self.generate(n, lp+1, rp, tmp, result)
            tmp.pop()
        if rp < lp:
            tmp.append(')')
            self.generate(n, lp, rp+1, tmp, result)
            tmp.pop()

    def generateParenthesis2(self, n):
        return list(self.generate2('', n, n))
        
    def generate2(self, p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in self.generate2(p + '(', left-1, right):
                yield q
            for q in self.generate2(p + ')', left, right-1):
                yield q
        
    
                
            
