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
        dummy = ListNode(None)
        ptr1 = l1
        ptr2 = l2
        ptr = dummy
        carry = 0
        while ptr1 or ptr2:
            carry /= 10
            if ptr1:
                carry += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                carry += ptr2.val
                ptr2 = ptr2.next
            ptr.next = ListNode(carry % 10)
            ptr = ptr.next
        if carry / 10 == 1:
            ptr.next = ListNode(1)
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :typ2 l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ''
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num = int(num1[::-1]) + int(num2[::-1])
        dummy = ListNode(None)
        ptr = dummy
        if num == 0:
            return ListNode(0)
        while num > 0:
            ptr.next = ListNode(num % 10)
            ptr = ptr.next
            num /= 10
        return dummy.next

    
