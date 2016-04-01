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
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == "0") or
                        (len(second) > 1 and second[0] == "0")):
                    continue

                while others:
                    sum_str = str(int(first) + int(second))
                    if sum_str == others:
                        return True
                    elif others.startswith(sum_str):
                        first, second, others = (
                            second, sum_str, others[len(sum_str):])
                    else:
                        break

        return False
