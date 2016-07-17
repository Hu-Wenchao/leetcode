"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? 
Would your previous solution still work?
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        prelayer = [root]
        while prelayer:
            for i in range(len(prelayer) - 1):
                prelayer[i].next = prelayer[i+1]
            curlayer = []
            for node in prelayer:
                if node.left:
                    curlayer.append(node.left)
                if node.right:
                    curlayer.append(node.right)
            prelayer = curlayer

    def connect2(self, root):
        dummy = TreeLinkNode(0)
        cur = dummy
        pre = root
        while pre:
            cur.next = pre.left
            if cur.next:
                cur = cur.next
            cur.next = pre.right
            if cur.next:
                cur = cur.next
            pre = pre.next
            if not pre:
                cur = dummy
                pre = dummy.next
