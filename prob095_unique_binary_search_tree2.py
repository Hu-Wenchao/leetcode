"""
Given n, generate all structurally unique BST's 
(binary search trees) that store values 1...n.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)
        
    def generate(self, first, last):
        trees = []
        for root in range(first, last+1):
            for left in self.generate(first, root-1):
                for right in self.generate(root+1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += node,
        return trees or [None]
 
