"""
Given a binary tree, check whether it is a mirror 
of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True

    
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isMirror(p.left, q.right) and \
                self.isMirror(p.right, q.left)
        else:
            return False

    
