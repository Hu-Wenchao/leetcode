"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of 
nodes from some starting node to any node in the tree 
along the parent-child connections. The path does not 
need to go through the root.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_value = -float('inf')
        self.maxPathDown(root)
        return self.max_value

    def maxPathDown(self, root):
        if not root:
            return 0
        left = max(0, self.maxPathDown(root.left))
        right = max(0, self.maxPathDown(root.right))
        self.max_value = max(self.max_value, left + right + root.val)
        return max(left, right) + root.val
