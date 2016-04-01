"""
You are given an integer array nums and you have to return a 
new counts array. The counts array has the property where 
counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def lowbit(self, i):
        return i & (-i)

    def add(self, c, n, i, val):
        while i<=n:
            c[i] += val
            i += self.lowbit(i)

    def getSum(self, c, i):
        res = 0
        while i>0:
            res += c[i]
            i -= self.lowbit(i)
        return res

    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        find_i = {}
        cnt = 1
        for n in sorted(nums):
            if n not in find_i:
                find_i[n] = cnt
                cnt += 1

        res = []
        c = [0 for i in range(cnt+1)]
        for i in range(len(nums)-1,-1,-1):
            res += self.getSum(c, find_i[nums[i]]-1),
            self.add(c, cnt, find_i[nums[i]], 1)
        return res[::-1]
