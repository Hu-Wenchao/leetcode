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
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            temp_list = []
            for i in range(0, len(lists) - 1, 2):
                merged_list = self.mergeLists(lists[i], lists[i+1])
                temp_list.append(merged_list)
            if len(lists)%2 == 1:
                temp_list.append(lists[len(lists) - 1])
            lists = temp_list
        return lists[0]

    def mergeLists(self, l1, l2):
        # merge two sorted list
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        ptr = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1 == None:
            ptr.next = l2
        else:
            ptr.next = l1
        return head
