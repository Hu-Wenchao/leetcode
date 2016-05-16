"""
Given a string containing only digits, restore it by returning 
all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        res = []
        for m in [1, 2, 3]:
            for n in [m+1, m+2, m+3]:
                for p in [n+1, n+2, n+3]:
                    if p >= len(s):
                        continue
                    s1, s2, s3, s4 = s[:m], s[m:n], s[n:p], s[p:]
                    if self.isValid([s1, s2, s3, s4]):
                        res.append(s1+'.'+s2+'.'+s3+'.'+s4)
        return res

    def isValid(self, str_list):
        for s in str_list:
            if s[0] == '0' and s != '0':
                return False
            elif int(s) > 255:
                return False
        return True
