"""
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
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
