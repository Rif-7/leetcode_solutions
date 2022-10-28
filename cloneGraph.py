from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class MySolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodeSet = {}
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            if n in nodeSet:
                continue
            nodeSet[n] = Node(n.val)
            q.extend(n.neighbors)
        
        for n, newNode in nodeSet.items():
            for neighbor in n.neighbors:
                newNode.neighbors.append(nodeSet[neighbor])
        
        return nodeSet[node]


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
        
        
        