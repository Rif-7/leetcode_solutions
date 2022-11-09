from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visit = set()
        minHeap = [[0, 0]]
        res = 0
        while len(visit) < N:
            c, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res += c
            for nei in adj[i]:
                if nei[1] not in visit:
                    heapq.heappush(minHeap, nei)
            
                
        
        
        return res