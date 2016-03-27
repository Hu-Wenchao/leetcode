"""
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = fast = head
        rev = ListNode(None)
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val == rev.val:
                slow = slow.next
                rev = rev.next
            else:
                return False
        return True
