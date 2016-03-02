"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.read(root, ret)
        return ret

    def read(self, root, ret):
        if root:
            self.read(root.left, ret)
            ret.append(root.val)
            self.read(root.right, ret)
