"""
Implement strStr().

Returns the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        for i in xrange(len(haystack) + 1):
            for j in xrange(len(needle) + 1):
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break

