"""
Given a sorted linked list, delete all nodes that 
have duplicate numbers, leaving only distinct 
numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while ptr.next:
            if ptr.next.next and ptr.next.val == ptr.next.next.val:
                tmpval = ptr.next.val
                while ptr.next and ptr.next.val == tmpval:
                    ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy.next
        dic = {}
        while ptr.next:
            if ptr.val == ptr.next.val:
                dic[ptr.val] = True
            ptr = ptr.next
        ptr = dummy
        while ptr.next:
            if ptr.next.val in dic:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
