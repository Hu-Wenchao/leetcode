"""
Given a linked list, return the node where the cycle 
begins. If there is no cycle, return null.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        hare, turtle = head, head
        while hare:
            turtle = turtle.next
            hare = hare.next
            if not hare:
                return None
            hare = hare.next
            if hare == turtle:
                turtle = head
                while turtle != hare:
                    turtle = turtle.next
                    hare = hare.next
                return hare
        return None
