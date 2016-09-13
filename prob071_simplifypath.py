"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)    
