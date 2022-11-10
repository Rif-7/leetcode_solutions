from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append([t, d])
        
        visit = set()
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [t+w2, n2])
        return t if len(visit) == n else -1
                
                    
        
        
        
        
        