from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap) + 1
                if curr:
                    q.append([curr, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                
        