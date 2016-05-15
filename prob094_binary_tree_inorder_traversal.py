"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    def inorderTraversal2(self, root):
        ret, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                ret.append(tmp.val)
                root = tmp.right
        return ret

    def inorderTraversal3(self, root):
        return self.inorderTraversal3(root.left) + \
            [root.val] + self.inorderTraversal3(root.right) if root else []
