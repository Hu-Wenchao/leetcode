"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        previousRow = [True]
        for i in range(0, len(p)):
            if p[i]=='*':
                previousRow.append(previousRow[i-1])
            else:
                previousRow.append(False)
        print(previousRow)
                
        for letter in range(0,len(s)):
            actualRow = [False];
            for i in range(0, len(p)):
                if p[i]=='*':
                    temp = actualRow[i-1] or \
                           (previousRow[i+1] and
                            (p[i-1]==s[letter] or p[i-1]=='.'))
                elif p[i] == '.':
                    temp = previousRow[i]
                else:
                    temp = previousRow[i] and p[i]==s[letter] 
                actualRow.append(temp)
            print(letter)
            print(actualRow)
            previousRow = actualRow
            print(previousRow)
        return previousRow[len(p)]
            
