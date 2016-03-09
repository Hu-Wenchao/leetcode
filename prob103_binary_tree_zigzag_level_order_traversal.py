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
        ret = []
        pre = []
        if root:
            pre.append(root)
            flag = 0
        while pre:
            temp = []
            cur = []
            flag += 1
            for node in pre:
                temp.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            pre = cur
            if flag % 2 == 1:
                ret.append(temp)
            else:
                temp.reverse()
                ret.append(temp)
        return ret
