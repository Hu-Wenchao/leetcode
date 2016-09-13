"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.inorder(root, res)
        first = None
        second = None
        for i in range(1, len(res)):
            if not first and res[i-1].val > res[i].val:
                first, second = res[i-1], res[i]
            if first and res[i-1].val > res[i].val:
                second = res[i]
        first.val, second.val = second.val, first.val

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root)
            self.inorder(root.right, res)
