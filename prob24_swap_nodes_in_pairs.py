"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not 
modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pt = dummy
        while pt.next and pt.next.next:
            tmp = pt.next.next
            pt.next.next = tmp.next
            tmp.next = pt.next
            pt.next = tmp
            pt = pt.next.next
        return dummy.next
