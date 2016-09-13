"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        prelayer = [root]
        while prelayer:
            curlayer = []
            for node in prelayer:
                if node.left:
                    curlayer.append(node.left)
                if node.right:
                    curlayer.append(node.right)
            res += 1
            prelayer = curlayer
        return res

    def maxDepth2(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth2(root.left), self.maxDepth2(root.right))
