"""
Merge k sorted linked lists and return it as
one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists)-1, 2):
                merged = self.merge(lists[i], lists[i+1])
                temp.append(merged)
            if len(lists) % 2 == 1:
                temp.append(lists[-1])
            lists = temp
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode(None)
        ptr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        if not l2:
            ptr.next = l1
        else:
            ptr.next = l2
        return dummy.next
