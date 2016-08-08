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
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        ptri = dummy.next
        while ptri:
            while ptri.next and ptri.next.val > ptri.val:
                ptri = ptri.next
            if not ptri.next:
                return dummy.next
            else:
                tmp = ptri.next
                ptri.next = ptri.next.next
            ptrj = dummy
            while ptrj.next.val < tmp.val:
                ptrj = ptrj.next
            tmp.next = ptrj.next
            ptrj.next = tmp

