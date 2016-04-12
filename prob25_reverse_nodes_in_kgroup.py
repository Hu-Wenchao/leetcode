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
        dummy = ListNode(0)
        previous = dummy
        dummy.next = head
        while True:
            begin = previous.next
            end = previous
            for i in range(k):
                end = end.next
                if end == None:
                    return dummy.next
            nextGroup = end.next
            self.reverseList(begin, end)
            previous.next = end
            begin.next = nextGroup
            previous = begin

    def reverseList(self, start, end):
        alreadyReversed = start
        actual = start
        nextNode = start.next
        while actual != end:
            actual = nextNode
            nextNode = nextNone.next
            actual.next = alreadyReversed
            alreadyReversed = actual
