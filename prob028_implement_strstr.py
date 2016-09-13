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
        i, j, m, n = -1, 0, len(haystack), len(needle)
        prefix = [-1] * n
        while j < n - 1:
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                prefix[j] = i
            else:
                i = prefix[i]
        i, j = 0, 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = prefix[j]
        if j == n:
            return i - j
        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


