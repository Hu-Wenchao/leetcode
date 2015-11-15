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
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        if head.next == None:
            return None

        # measure the length of the list:
        ptr = head
        list_length = 1
        while ptr.next != None:
            list_length += 1
            ptr = ptr.next
        
        # n == list_length case
        if n == list_length:
            return head.next

        # move the pointer to (list_length - n)'s position.
        posi = list_length - n 
        ptr = head
        while posi > 1:
            posi -= 1
            ptr = ptr.next
        
        # n == 1 case
        if n == 1:
            ptr.next = None
        else:
            ptr.next = ptr.next.next

        return head
