"""
Given a linked list, remove the nth node from the end of
list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        l = 0
        while ptr.next:
            l += 1
            ptr = ptr.next
        ptr = dummy
        while l - n > 0:
            ptr = ptr.next
            l -= 1
        ptr.next = ptr.next.next
        return dummy.next
