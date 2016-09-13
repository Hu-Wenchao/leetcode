"""
All DNA is composed of a series of nucleotides abbreviated 
as A, C, G, and T, for example: "ACGAATTCCG". When studying 
DNA, it is sometimes useful to identify repeated sequences 
within the DNA.

Write a function to find all the 10-letter-long sequences 
(substrings) that occur more than once in a DNA molecule.
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seq = {}
        for i in range(len(s) - 9):
            if s[i:i+10] not in seq:
                seq[s[i:i+10]] = 1
            else:
                seq[s[i:i+10]] += 1
        return [key for key, value in seq.iteritems() if value > 1]
