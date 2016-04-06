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
        pre = head
        cur = head.next
        while cur:
            if cur.val < pre.val:
                temp = pre
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                temp.next = cur.next
                cur.next = pre.next
                pre.next = cur
                cur = temp.next
                pre = temp
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
            

    def insetionSortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(None)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            temp = cur.next
            cur.next = temp.next
            temp.next = p.next
            p.next = temp
        return dummy.next

