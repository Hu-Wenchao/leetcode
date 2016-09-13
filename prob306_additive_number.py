"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the 
sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an 
additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive 
sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = len(num)
        for i in range(1, l/2+1):
            for j in range(1, (l-i)/2+1):
                first, second, rest = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == "0") or
                        (len(second) > 1 and second[0] == "0")):
                    continue
                while rest:
                    sum_str = str(int(first) + int(second))
                    if sum_str == rest:
                        return True
                    elif rest.startswith(sum_str):
                        first, second, rest = (
                            second, sum_str, rest[len(sum_str):])
                    else:
                        break
        return False
