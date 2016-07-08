"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n:
            return head
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        for i in xrange(m - 1):
            ptr = ptr.next
        pre = ptr
        tail = ptr.next
        cur = ptr.next
        while ptr.next and n - m >= 0:
            tmp = cur.next
            cur.next = ptr
            ptr = cur
            cur = tmp
            n -= 1
        pre.next = ptr
        tail.next = cur
        return dummy.next
            
        
