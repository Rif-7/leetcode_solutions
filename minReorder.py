from collections import deque

class Solution:
    def minReorder(self, n: int, connections) -> int:
        neighs = deque()
        count = 0
        edges = { (a, b) for a, b in connections }
        changes = 0
        visit = set()
        neighbors = { city: set() for city in range(n)}

        for a, b in connections:
            neighbors[a].add(b)
            neighbors[b].add(a)

        def dfs(city):
            nonlocal changes

            for nei in neighbors[city]:
                if nei in visit:
                    continue
                if (nei, city) not in edges:
                    changes += 1
                visit.add(nei)
                dfs(nei)
        visit.add(0)
        dfs(0)
    
        return changes