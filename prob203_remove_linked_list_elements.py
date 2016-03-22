"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = pre = ListNode(None)
        dummy.next = head
        cur = pre.next
        while cur.next:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        if cur.val == val:
            pre.next = None
        return dummy.next
