"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""
import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1
        try:
            float(s)
            return True
        except ValueError:
            return False

        # Solution 2 using re
        return bool(re.match('[\+\-]?((\d*\.?\d+)|(\d+\.?\d*))([eE][\+\-]?\d+)?$',\
                             s.strip()))

