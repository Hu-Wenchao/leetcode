"""
Given a complete binary tree, count the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ld = self.depth(root.left)
        rd = self.depth(root.right)
        if ld == rd:
            return 2**ld + self.countNodes(root.right)
        else:
            return 2**rd + self.countNodes(root.left)

    def depth(self, root):
        if not root:
            return 0
        return 1 + self.depth(root.left)
