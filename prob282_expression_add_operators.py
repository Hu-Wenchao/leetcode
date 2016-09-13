"""
Given a string that contains only digits 0-9 and a target value, 
return all possibilities to add binary operators (not unary) +, -, 
or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]),
                         res, target)
        return res
        
    def dfs(self, num, tmp, cur, last, res, target):
        if not num:
            if cur == target:
                res.append(tmp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], tmp + '+' + val, cur + int(val),
                         int(val), res, target)
                self.dfs(num[i:], tmp + '-' + val, cur - int(val),
                         -int(val), res, target)
                self.dfs(num[i:], tmp + '*' + val, cur - last + last * int(val),
                         last * int(val), res, target)
