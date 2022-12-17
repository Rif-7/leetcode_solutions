from collections import defaultdict

class Solution:
    def leastBricks(self, wall) -> int:
        gapMap = defaultdict(int)
        res = 0
        for row in wall:
            offset = 0
            for c in range(len(row) - 1):
                offset += row[c]
                gapMap[offset] += 1
                res = max(res, gapMap[offset]) 
                
        return len(wall) - res
        