"""
Given a linked list, reverse the nodes of a linked list
k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out 
nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes 
itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        l = 0
        while ptr.next:
            l += 1
            ptr = ptr.next
        ptr = dummy
        cur = ptr.next
        n = l / k
        for i in xrange(n):
            pre = ptr
            tail = cur
            for j in xrange(k):
                tmp = cur.next
                cur.next = ptr
                ptr = cur
                cur = tmp
            pre.next = ptr
            tail.next = cur
            ptr = tail
            cur = ptr.next
        return dummy.next
    
    def reverseKGroup2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while True:
            head = ptr.next
            tail = ptr
            for i in range(k):
                tail = tail.next
                if tail == None:
                    return dummy.next
            next_group = tail.next
            self.reverse(head, tail)
            ptr.next = tail
            head.next = next_group
            ptr = head
        
    def reverse(self, head, tail):
        reversed = head
        cur = head
        next_node = head.next
        while cur != tail:
            cur = next_node
            next_node = next_node.next
            cur.next = reversed
            reversed = cur
