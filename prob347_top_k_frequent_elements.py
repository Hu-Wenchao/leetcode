"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        arr = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        res = []
        for n in arr[:k]:
            res.append(n[0])
        return res
    
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        tmp = Counter(nums).most_common(k)
        res = [n[0] for n in tmp]
        return res
