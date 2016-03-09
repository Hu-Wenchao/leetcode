"""
Given a binary tree, check whether it is a mirror 
of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.symmetricTree(root.left, root.right)

    def symmetricTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.symmetricTree(p.left, q.right) and \
                self.symmetricTree(p.right, q.left)
        else:
            return False
