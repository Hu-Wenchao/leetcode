"""
Given a list, rotate the list to the right by k places, 
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        # Measure the list length.
        l = 0
        ptr = dummy
        while ptr.next:
            ptr = ptr.next
            l += 1
        # Make circular list.
        ptr.next = head
        # Compute the offset.
        n = l - k % l        
        # Move the cursor to nth place.
        ptr = dummy
        while n > 0:
            ptr = ptr.next
            n -= 1        
        # Break the cicular list.
        head = ptr.next
        ptr.next = None
        return head
