"""
For a undirected graph with tree characteristics, we can choose 
any node as the root. The result graph is then a rooted tree. 
Among all possible rooted trees, those with minimum height are 
called minimum height trees (MHTs). Given such a graph, write a 
function to find all the MHTs and return a list of their root labels
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        neighbor = [set() for _ in xrange(n)]
        for i, j in edges:
            neighbor[i].add(j)
            neighbor[j].add(i)
        leaves = [i for i in xrange(n) if len(neighbor[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = neighbor[i].pop()
                neighbor[j].remove(i)
                if len(neighbor[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
