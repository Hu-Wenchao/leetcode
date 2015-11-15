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
        solution = []
        self.generateParenthesisRec(n, 0, 0, [], solution)
        return solution
        
    def generateParenthesisRec(self, n, openParenthesis, 
                               closeParenthesis, tempSolution, solution): 
        if closeParenthesis == n:
            solution.append("".join(tempSolution))
            return
        if openParenthesis < n:
            tempSolution.append("(")
            self.generateParenthesisRec(n, openParenthesis+1, 
                                        closeParenthesis, tempSolution, 
                                        solution)
            tempSolution.pop()
        if closeParenthesis < openParenthesis:
            tempSolution.append(")")
            self.generateParenthesisRec(n, openParenthesis, 
                                        closeParenthesis+1, tempSolution, 
                                        solution)
            tempSolution.pop()
                    
                
            
