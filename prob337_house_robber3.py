"""
The thief has found himself a new place for his thievery 
again. There is only one entrance to this area, called 
the "root." Besides the root, each house has one and only 
one parent house. After a tour, the smart thief realized 
that "all houses in this place forms a binary tree". It 
will automatically contact the police if two directly-
linked houses were broken into on the same night.

Determine the maximum amount of money the thief can 
rob tonight without alerting the police.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robsub(root)
        return max(res)

    def robsub(self, root):
        if not root:
            return [0, 0]
        left = self.robsub(root.left)
        right = self.robsub(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res
