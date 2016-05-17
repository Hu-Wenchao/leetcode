"""
Given a binary tree, return the bottom-up level order 
traversal of its nodes' values. (ie, from left to right, 
level by level from leaf to root).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        prelayer = [root]
        while prelayer:
            curlayer = []
            tmp = []
            for node in prelayer:
                tmp.append(node.val)
                if node.left:
                    curlayer.append(node.left)
                if node.right:
                    curlayer.append(node.right)
            res.insert(0, tmp)
            prelayer = curlayer
        return res
