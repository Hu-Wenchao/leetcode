"""
A linked list is given such that each node contains 
an additional random pointer which could point to 
any node in the list or null.
Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        ptr = head
        while ptr:
            dic[ptr] = RandomListNode(ptr.label)
            ptr = ptr.next
        ptr = head
        while ptr:
            dic[ptr].next = dic.get(ptr.next)
            dic[ptr].random = dic.get(ptr.random)
            ptr = ptr.next
        return dic.get(head)
