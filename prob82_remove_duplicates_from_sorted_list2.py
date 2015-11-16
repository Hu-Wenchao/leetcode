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
        dummy = ListNode(0)
        list = dummy
        pointer = head
        while pointer!= None:
            if pointer.next != None and pointer.val == pointer.next.val:
                value = pointer.val;
                while pointer!= None and pointer.val == value:
                    pointer = pointer.next
            else:
                list.next = pointer
                list = list.next
                pointer = pointer.next
        list.next = None
        return dummy.next
