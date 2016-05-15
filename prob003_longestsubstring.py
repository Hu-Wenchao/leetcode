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
        ret, tmp = 0, []
        for i in xrange(len(s)):
            if s[i] not in tmp:
                tmp.append(s[i])
            else:
                if ret < len(tmp):
                    ret = len(tmp)
                del tmp[:tmp.index(s[i]) + 1]
                tmp.append(s[i])
        if ret < len(tmp):
            ret = len(tmp)
        return ret

    def lengthOfLongestSubstring2(self, s):
        ret, start, d = 0, 0, {}
        for i, ch in enumerate(s):
            if ch in d:
                ret = max(ret, i - start)
                start = max(start, d[ch] + 1)
            d[ch] = i
        return max(ret, len(s) - start)
