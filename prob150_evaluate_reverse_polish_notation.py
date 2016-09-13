"""
Evaluate the value of an arithmetic expression in 
Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be 
an integer or another expression.
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            if s not in ['+', '-', '*', '/']:
                stack.append(int(s))
            else:
                a, b = stack.pop(), stack.pop()
                if s == '+':
                    stack.append(b + a)
                elif s == '-':
                    stack.append(b - a)
                elif s == '*':
                    stack.append(b * a)
                else:
                    if b * a < 0 and b % a != 0:
                        stack.append(b / a + 1)
                    else:
                        stack.append(b / a)
        return stack.pop()
                
