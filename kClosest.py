import heapq
import math
class Solution:
    def kClosest(self, points, k: int):
        pts = []
        for p in points:
            dis = self.distance(p)
            pts.append([dis, p])
            
        heapq.heapify(pts)
        res = []
        for i in range(k):
            d, p = heapq.heappop(pts)
            res.append(p)
        return res
            
            
    def distance(self, cords):
        return math.sqrt(math.pow(0 - cords[0], 2) + math.pow(0 - cords[1], 2))