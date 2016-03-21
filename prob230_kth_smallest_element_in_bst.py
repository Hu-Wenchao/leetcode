"""
Given a binary search tree, write a function 
kthSmallest to find the kth smallest element in it.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        tree = self.inOrder(root, [])
        return tree[k-1]
        
    def inOrder(self, root, ret):
        if root:
            self.inOrder(root.left, ret)
            ret.append(root.val)
            self.inOrder(root.right, ret)
        return ret
