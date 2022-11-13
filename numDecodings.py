class MySolution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        res = [-1] * N
        
        def dfs(i):
            if i >= N:
                return 1
            if s[i] == "0":
                return 0
            if res[i] != -1:
                return res[i]
            
            ans = dfs(i+1)
            if (i + 1 < N and
               int(s[i: i+2]) <= 26):     
                ans += dfs(i+2)
            
            res[i] = ans 
            return ans
        
        return dfs(0)

class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)