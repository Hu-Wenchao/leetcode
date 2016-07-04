"""
You have a number of envelopes with widths and heights 
given as a pair of integers (w, h). One envelope can 
fit into another if and only if both the width and 
height of one envelope is greater than the width and 
height of the other envelope.

What is the maximum number of envelopes can you Russian 
doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum 
number of envelopes you can Russian doll is 3 
([2,3] => [5,4] => [6,7]).
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(cmp = lambda x,y:
                       x[0]-y[0] if x[0] != y[0] else y[1]-x[1])
        tails = []
        for i in range(len(envelopes)):
            e = envelopes[i]
            p = self.bin_search(tails, e)
            if p == len(tails):
                tails.append(e)
            else:
                tails[p] = e
        return len(tails)
        
    def bin_search(self, A, key):
        l, r = 0, len(A)
        while l < r:
            mid = (l + r) / 2
            if A[mid][1] < key[1]:
                l = mid + 1
            else:
                r = mid
        return l
