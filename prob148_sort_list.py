"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        middle = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(middle))

    def merge(self, h1, h2):
        dummy = ListNode(None)
        ptr = dummy
        while h1 and h2:
            if h1.val < h2.val:
                ptr.next = h1
                ptr = ptr.next
                h1 = h1.next
            else:
                ptr.next = h2
                ptr = ptr.next
                h2 = h2.next
        ptr.next = h1 or h2
        return dummy.next
