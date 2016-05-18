"""
Write a function that takes a string as input and 
reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        tmp = list(s)
        l, r = 0, len(tmp)-1
        while l < r:
            while l < r and tmp[l] not in 'aeiouAEIOU':
                l += 1
            while l < r and tmp[r] not in 'aeiouAEIOU':
                r -= 1
            tmp[l], tmp[r] = tmp[r], tmp[l]
            l += 1
            r -= 1
        return ''.join(tmp)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
