"""
Clone an undirected graph. Each node in the graph 
contains a label and a list of its neighbors.
"""

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(dic[neighbor])
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    def cloneGraph2(self, node):
        if not node:
            return 
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(dic[neighbor])
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
            
    def cloneGraph3(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(dic[neighbor])
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])
