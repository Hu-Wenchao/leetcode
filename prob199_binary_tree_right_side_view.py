"""
Given a binary tree, imagine yourself standing on the 
right side of it, return the values of the nodes you 
can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        prelayer = [root]
        res = [root.val]
        while prelayer:
            curlayer = []
            for node in prelayer:
                if node.left:
                    curlayer.append(node.left)
                if node.right:
                    curlayer.append(node.right)
            if curlayer:
                res.append(curlayer[-1].val)
            prelayer = curlayer
        return res
