from collections import deque
import math

class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(1, n)])
        while q:
            l, val = q.popleft()
            if self.isPerfect(val):
                return l
            for i in range(1, val):
                if not self.isPerfect(i):
                    continue
                q.append((l + 1, val - i))


    def isPerfect(self, val):
        return math.sqrt(val) == int(math.sqrt(val))


class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def dfs(val):
            if val in dp:
                return dp[val]
            if val == 1:
                return 1

            if self.isPerfect(val):
                return 1

            res = float("inf")
            for i in range(1, val):
                if not self.isPerfect(i):
                    continue
                res = min(res, 1 + dfs(val - i))
            dp[val] = res
            return res

        return dfs(n)

    def isPerfect(self, val):
        return math.sqrt(val) == int(math.sqrt(val))
            

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        
        return dp[n]