"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorder(root, res)
        return res
        
    def postorder(self, root, res):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)

    def postorderTraversal2(self, root):
        res, stack = [], [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                res.append(tmp.val)
                stack.append(tmp.left)
                stack.append(tmp.right)
        return res[::-1]
