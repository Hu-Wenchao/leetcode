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
            return head
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while ptr.next:
            if ptr.next.val != val:
                ptr = ptr.next
            else:
                if ptr.next.next:
                    ptr.next = ptr.next.next
                else:
                    ptr.next = None
        return dummy.next
