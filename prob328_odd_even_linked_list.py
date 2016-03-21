"""
Given a singly linked list, group all odd nodes 
together followed by the even nodes. Please note 
here we are talking about the node number and not 
the value in the nodes.

You should try to do it in place. The program should 
run in O(1) space complexity and O(nodes) time complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        oddptr = odd
        evenptr = even
        head = head.next.next
        while head and head.next:
            oddptr.next = head
            evenptr.next = head.next
            oddptr = oddptr.next
            evenptr = evenptr.next
            head = head.next.next
        if head:
            oddptr.next = head
            oddptr = oddptr.next
        evenptr.next = None
        oddptr.next = even
        return odd
