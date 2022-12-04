import heapq

class MySolution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        res = [0] * len(queries)
        queries = sorted([[v, i] for i, v in enumerate(queries)])
        minH = []
        
        j = 0
        i = 0
        while j < len(queries):
            while i < len(intervals) and intervals[i][0] <= queries[j][0]:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minH, [size, intervals[i][1]])
                i += 1
            
            while minH and minH[0][1] < queries[j][0]:
                heapq.heappop(minH)
            
            res[queries[j][1]] = minH[0][0] if minH else -1
            j += 1
        return res
        

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]




