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
        if len(s)== 0: 
            return 0
        ls = list(s.strip())
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = 10 * ret + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret, 2**31 - 1))

    def myAtoi2(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0
