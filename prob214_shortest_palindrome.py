"""
Given a string S, you are allowed to convert it to a 
palindrome by adding characters in front of it. Find 
and return the shortest palindrome you can find by 
performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # using the KMP table
        A = s + '*' + s[::-1]
        table = [0]
        for i in xrange(1, len(A)):
            index = table[i-1]
            while index > 0 and A[index] != A[i]:
                index = table[index-1]
            table.append(index + (1 if A[index] == A[i] else 0))
        return s[table[-1]:][::-1] + s
