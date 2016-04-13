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
        ret = []
        self.helper(root, ret)
        return ret
        
    def helper(self, root, ret):
        if root:
            self.helper(root.left, ret)
            self.helper(root.right, ret)
            ret.append(root.val)

    def postorderTraversal2(self, root):
        ret, stack = [], [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                ret.append(tmp.val)
                stack.append(tmp.left)
                stack.append(tmp.right)
        return ret[::-1]

    def postorderTraversal3(self, root):
        return self.postorderTraversal3(root.left) + \
            self.postorderTraversal3(root.right) + [root.val] if root else []
