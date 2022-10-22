import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            l1 = heapq.heappop(stones) * -1
            l2 = heapq.heappop(stones) * -1
            if l1 != l2:
                heapq.heappush(stones, (l1 - l2) * -1)
        
        return stones[0] * -1 if stones else 0