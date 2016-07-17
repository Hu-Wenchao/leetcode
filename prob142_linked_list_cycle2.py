"""
Given a linked list, return the node where the cycle 
begins. If there is no cycle, return null.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        while fast:
            slow, fast = slow.next, fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return fast
        return None
