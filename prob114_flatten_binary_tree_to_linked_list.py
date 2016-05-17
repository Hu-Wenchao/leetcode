"""
Given a binary tree, flatten it to a linked list in-place.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # n is the current visiting node
        # p is the previous node of preorder traversal to n.right
        # we need to do the inorder replacement
        # n.left -> Null
        # n.right -> n.left
        # p.right -> n.right
        if not root:
            return
        self.prev = root
        self.flatten(root.left)        
        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp        
        self.flatten(temp)
