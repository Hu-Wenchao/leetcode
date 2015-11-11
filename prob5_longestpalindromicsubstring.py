"""
Given a string S, find the longest palindromic 
substring in S. You may assume that the maximum
length of S is 1000, and there exists one unique
longest palindromic substring.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = self.preProcess(s)
        n = len(t)
        # Taking t[i] as center, check both left and right,
        # T[i] itself not included, p[i] is the length
        # of palindromic substring in original string s.
        p = [0] * n
        c = 0
        r = 0
        
        for i in range(1, n-1):
            i_mirror = 2 * c - i  # equals to i' = c - (i-c)
            p[i] = min(r - i, p[i_mirror]) if r > i else 0
            
            while t[i+1+p[i]] == t[i-1-p[i]]:
                p[i] += 1
            if i+p[i] > r:
                c = i
                r = i + p[i]

        max_len = 0
        center_index = 0
        for i in range(1, n-1):
            if p[i] > max_len:
                max_len = p[i]
                center_index = i
        
        return s[(center_index - 1 - max_len) / 2 :
                 (center_index - 1 + max_len) / 2]

    def preProcess(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end
        # to avoid bounds checking.
        n = len(s)
        if n == 0:
            return "^$"
        ret = "^"
        for i in range(n):
            ret += "#" + s[i]
        ret += "#$"
        return ret


    def longestPalindrome2(self, s):
        # brute force method, not accepted.
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or (len(s) == 2 and s[0] == s[1]):
            return s
        strlength = 1
        location = 0
        strtype = "odd"
        for i in range(len(s) - 1):
            k = 1
            tempstrlength = 1
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                tempstrlength += 2
                k += 1
            if tempstrlength > strlength:
                strlength = tempstrlength
                location = i
                strtype = "odd"

            k = 1
            tempstrlength = 2
            while i-k >= 0 and i+k+1 < len(s) and s[i-k] == s[i+k+1]:
                tempstrlength += 2
                k += 1
            if tempstrlength > strlength:
                strlength = tempstrlength
                location = i
                strtype = "even"

        if strtype is "odd":
            return s[location - strlength/2 : location + strlength/2 + 1]
        else:
            return s[location - strlength/2 + 1 : location + strlength/2 + 1]
