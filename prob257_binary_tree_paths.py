"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.path(root, [], res)
        return res

    def path(self, root, tmplist, res):
        if not root.left and not root.right:
            res.append('->'.join(map(str, tmplist + [root.val])))
        if root.left:
            self.path(root.left, tmplist + [root.val], res)
        if root.right:
            self.path(root.right, tmplist + [root.val], res)
