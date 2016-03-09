"""
Given a binary tree, return the level order traversal 
of its nodes' values. (ie, from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        pre = []
        if root:
            pre.append(root)
        while pre:
            temp = []
            cur = []
            for node in pre:
                temp.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            pre = cur
            ret.append(temp)
        return ret
