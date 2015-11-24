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
        mydict = {}
        for word in strs:
            temp = "".join(sorted(word))
            mydict[temp] = [word] if temp not in mydict \
                           else mydict[temp] + [word]
        res = []
        for key in mydict:
            item_list = mydict[key]
            item_list.sort()
            res.append(item_list)
        return res
