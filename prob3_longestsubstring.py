"""
Given a string, find the length of the longest substring
without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is
"abc", which the length is 3. For "bbbbb" the longest
substring is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlength = 0
        templist = []
        for i in range(len(s)):
            if s[i] not in templist:
                templist += [s[i]]
            else:
                if strlength < len(templist):
                    strlength = len(templist)
                del templist[:templist.index(s[i])+1]
                templist += s[i]
        if strlength < len(templist):
            strlength = len(templist)
        return strlength
