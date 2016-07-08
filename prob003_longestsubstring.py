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
        res = 0
        stack = []
        for c in s:
            if c not in stack:
                stack.append(c)
            else:
                res = max(res, len(stack))
                stack.append(c)
                del stack[:stack.index(c)+1]
        res = max(res, len(stack))
        return res

    def lengthOfLongestSubstring2(self, s):
        res = 0
        dic = {}
        start = 0
        for i, c in enumerate(s):
            if c in dic:
                res = max(res, i - start)
                start = max(start, dic[c] + 1)
            dic[c] = i
        return max(res, len(s) - start)
