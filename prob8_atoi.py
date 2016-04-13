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
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        i, value = 0, 0
        if s[0] in ['-', '+']:
            i += 1
        while i < len(s) and s[i].isdigit():
            value = 10 * value + ord(s[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * value, 2**31 - 1))

    def myAtoi2(self, s):
        s = s.strip()
        s = re.findall('^[\+\-0]?\d+', s)
        try:
            result = int(s[0])
            return min(max(result, -2**31), 2**31-1)
        except:
            return 0
