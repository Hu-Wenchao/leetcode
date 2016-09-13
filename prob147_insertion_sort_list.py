"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# According to the comments, a better way to sort a linked list is
# to copy them into a array and use quicksort to do the sort.
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        i = dummy.next
        while i.next:
            if i.val <= i.next.val:
                i = i.next
                continue
            else:
                j = dummy
                while j.next.val < i.next.val:
                    j = j.next
                tmp = j.next
                j.next = i.next
                i.next = i.next.next
                j.next.next = tmp
        return dummy.next

