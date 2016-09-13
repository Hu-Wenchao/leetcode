"""
Given n, generate all structurally unique BST's 
(binary search trees) that store values 1...n.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)
        
    def generate(self, begin, end):
        trees = []
        for root in range(begin, end+1):
            for left in self.generate(begin, root-1):
                for right in self.generate(root+1, end):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees or [None]
 
