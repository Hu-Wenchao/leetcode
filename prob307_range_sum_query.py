"""
Given an integer array nums, find the sum of the elements 
between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the 
element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums, self.tree = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.tree[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff, self.nums[i] = val - self.nums[i], val
        i += 1
        while i <= self.n:
            self.tree[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res, j = 0, j + 1
        while j:
            res += self.tree[j]
            j -= (j & -j)
        while i:
            res -= self.tree[i]
            i -= (i & -i)
        return res


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
