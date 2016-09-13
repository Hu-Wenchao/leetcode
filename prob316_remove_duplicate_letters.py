"""
Given a string which contains only lowercase letters, 
remove duplicate letters so that every letter appear 
once and only once. You must make sure your result is 
the smallest in lexicographical order among all 
possible results.
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        res = ''
        used = [False] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in s:
            ci = ord(c) - ord('a')
            cnt[ci] -= 1
            if used[ci]:
                continue
            for j in xrange(len(res)-1, -1, -1):
                cj = ord(res[j]) - ord('a')
                if cj > ci and cnt[cj] > 0:
                    used[cj] = False
                    res = res[:j] + res[j+1:]
                else:
                    break
            used[ci] = True
            res += c
        return res
