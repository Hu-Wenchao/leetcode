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
        if k == 0 or head == None or head.next == None:
            return head

        ptr = head
        # Measure the list length.
        l = 1
        while ptr.next:
            l += 1
            ptr = ptr.next

        # Make circular list.
        ptr.next = head

        # Compute the offset.
        n = l - k % l
        
        # Move the cursor to nth place.
        while n > 0:
            ptr = head
            head = head.next
            n -= 1
        
        # Break the cicular list.
        ptr.next = None

        return head
