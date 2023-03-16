import math


class Solution:
    def eliminateMaximum(self, dist, speed) -> int:
        minReach = []
        for d, s in zip(dist, speed):
            minReach.append(math.ceil(d / s))

        minReach.sort()
        res = 0
        for m in range(len(minReach)):
            if m >= minReach[m]:
                return res
            res += 1
        return res
