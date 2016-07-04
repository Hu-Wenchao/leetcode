"""
Given an integer array nums, return the number of range sums 
that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums 
between indices i and j (i ≤ j), inclusive.
"""
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    
    
    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx
    
    
    def get(self, idx):
        s = 0
        while idx:
            s += self.tree[idx]
            idx -= idx & -idx
        return s
    
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        T, d, pref = self.build_bit(nums, lower, upper)
        return self.compute_count(T, d, pref, lower, upper)

    def build_prefix(self, nums):
        sums, res = 0, []
        for elem in nums:
            sums += elem
            res.append(sums)
        res.insert(0, 0)
        return res

    def build_bit(self, nums, low, up):
        pref, vals = self.build_prefix(nums), set()
        for e in pref:
            vals |= set([e + low, e + up, e])
        d = {v: i for i, v in enumerate(sorted(list(vals)))}
        T = BinaryIndexedTree(len(d))
        return T, d, pref

    def compute_count(self, T, d, pref, low, up):
        count, n = 0, len(T.tree)
        for elem in pref[::-1]:
            lb, ub = elem + low, elem + up
            count += T.get(d[ub] + 1) - T.get(d[lb])
            T.update(d[elem] + 1, 1)
        return count
