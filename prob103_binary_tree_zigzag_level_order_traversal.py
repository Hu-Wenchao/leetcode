"""
Given a binary tree, return the zigzag level order 
traversal of its nodes' values. (ie, from left to right, 
then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        prelayer = [root]
        flag = 0  # 0 for forward, 1 for backward
        while prelayer:
            curlayer = []
            tmp = []
            for node in prelayer:
                tmp.append(node.val)
                if node.left:
                    curlayer.append(node.left)
                if node.right:
                    curlayer.append(node.right)
            if flag % 2 == 0:
                res.append(tmp)
                flag = 1
            else:
                res.append(tmp[::-1])
                flag = 0
            prelayer = curlayer
        return res
