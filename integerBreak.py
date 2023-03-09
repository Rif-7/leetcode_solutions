class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(val):
            if val in dp:
                return dp[val]

            if val == 1:
                return 1
            res = val
            for i in range(1, val):
                res = max(res, i * dfs(val - i))
            dp[val] = res
            return res
        
        res = 0
        for i in range(1, n):
            res = max(res, i * dfs(n - i))
        
        return res