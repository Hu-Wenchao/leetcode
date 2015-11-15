"""
Write a function to find the longest common
prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])-1, -1, -1):
            comPre = strs[0][:i+1]
            isValid = True
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][:i+1] != comPre:
                    isValid = False
                    break
            if isValid:
                return comPre

        return ""
