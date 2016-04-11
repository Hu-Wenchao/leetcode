"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, root, ret):
        if root:
            ret.append(root.val)
            self.helper(root.left, ret)
            self.helper(root.right, ret)

    def preorderTraversal2(self, root):
        ret, stack = [], [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                ret.append(tmp.val)
                stack.append(tmp.right)
                stack.append(tmp.left)
        return ret

    def preorderTraversal3(self, root):
        return [root.val] + self.preorderTraversal3(root.left) + \
            self.preorderTraversal3(root.right) if root else []
