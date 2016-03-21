"""
Write a program to find the node at which the 
intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 -> a2
                   \
                     c1 -> c2 -> c3
                   /            
B:     b1 -> b2 -> b3
begin to intersect at node c1.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa
