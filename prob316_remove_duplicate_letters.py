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
        lastAppear, inResult, result =  {c: i for i, c in enumerate(s)}, 0, []
        for i, c in enumerate(s):
            mask = 1 << (ord(c) - 97)
            if not (mask & inResult):
                while result and c < result[-1] and i < lastAppear[result[-1]]:
                    inResult ^= 1 << (ord(result.pop()) - 97)  # set to 0
                result.append(c)
                inResult |= mask  # set to 1
        return ''.join(result)

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        counts = collections.Counter(list(s))
        
        pos = 0
        for i, x in enumerate(s):
            if x < s[pos]: pos = i
            counts[x] -= 1
            if counts[x] == 0: break
            
        return s[pos] + \
            self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))
