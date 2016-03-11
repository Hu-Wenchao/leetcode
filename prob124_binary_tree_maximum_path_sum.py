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
    maxValue = -float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathDown(root)
        return self.maxValue

    def maxPathDown(self, node):
        if not node:
            return 0
        left = max(0, self.maxPathDown(node.left))
        right = max(0, self.maxPathDown(node.right))
        self.maxValue = max(self.maxValue, left + right + node.val)
        return max(left, right) + node.val
