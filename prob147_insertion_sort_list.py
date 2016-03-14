"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = cursor = dummy_head = ListNode(0)
        dummy_head.next = head
        
        while cursor.next:
            if pre.next.val > cursor.next.val:
                pre = dummy_head
            while pre.next.val < cursor.next.val:
                pre = pre.next
            if pre != cursor:
                node = cursor.next
                cursor.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cursor = cursor.next
        return dummy_head.next
            
