import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        charMap = defaultdict(int)
        for c in s:
            charMap[c] += 1
            
        minHeap = []
        for k, v in charMap.items():
            heapq.heappush(minHeap, (-v, k))
        
        res = ""
        prev = ()
        while minHeap:
            count, char = heapq.heappop(minHeap)
            res += char
            if prev:
                heapq.heappush(minHeap, prev)
                prev = ()
            if count + 1 != 0:
                prev = (count + 1, char)
    
        
        if not prev:
            return res
        
        return "" if res[-1] == prev[1] else res + prev[1]
        
            
        
            