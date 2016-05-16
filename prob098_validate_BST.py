"""
Given a binary tree, determine if it is a valid 
binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes 
with keys less than the node's key.
The right subtree of a node contains only nodes 
with keys greater than the node's key.
Both the left and right subtrees must also 
be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tree = []
        self.inOrder(root, tree)
        for i in xrange(1, len(tree)):
            if tree[i-1] >= tree[i]:
                return False
        return True

    def inOrder(self, root, tree):
        if not root:
            return
        self.inOrder(root.left, tree)
        tree.append(root.val)
        self.inOrder(root.right, tree)
        
            
