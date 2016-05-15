"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must 
follow the lexicographic order.
All inputs will be in lower-case.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            dic[key] = [word] if key not in dic else dic[key] + [word]
        ret = []
        for key in dic.keys():
            ret.append(sorted(dic[key]))
        return ret
