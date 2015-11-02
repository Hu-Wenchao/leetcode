"""
You are given two linked lists representing two non-negative
 numbers. The digits are stored in reverse order and each of
 their nodes contain a single digit. Add the two numbers and
 return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = l1
        carry = (l1.val + l2.val) // 10
        l1.val = (l1.val + l2.val) % 10
        while l1.next != None and l2.next != None:
            carry += l1.next.val + l2.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
            l2 = l2.next
        if l1.next == None:
            l1.next = l2.next
        while l1.next != None:
            carry += l1.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
        if carry:
            l1.next = ListNode(carry)
        return head
