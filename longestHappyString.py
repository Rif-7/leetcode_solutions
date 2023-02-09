import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(minHeap, (count, char))
        heapq.heapify(minHeap)
        res = ""
        while minHeap:
            count, char = heapq.heappop(minHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if minHeap:
                    count2, char2 = heapq.heappop(minHeap)
                    res += char2
                    count2 += 1
                    if count2:
                        heapq.heappush(minHeap, (count2, char2))
                else:
                    break
            else:
                res += char
                count += 1
            
            if count:
                heapq.heappush(minHeap, (count, char))
            
            
        return res