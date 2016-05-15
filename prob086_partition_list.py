"""
Given a linked list and a value x, partition it such that 
all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the 
nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head

        # Find the first node where node.val >= x
        ptr = head
        if ptr.val >= x:
            small = dummy
            large = head
        else:
            while ptr.next and ptr.next.val < x:
                ptr = ptr.next
            if not ptr.next:
                return head
            else:
                small = ptr
                large = ptr.next
        
        # partition the list
        while ptr.next:
            while ptr.next and ptr.next.val < x:
                small.next = ptr.next
                small = small.next
                ptr.next = ptr.next.next
            if ptr.next:
                ptr = ptr.next
        small.next = large
        
        if head.val >= x:
            return dummy.next
        else:
            return head
