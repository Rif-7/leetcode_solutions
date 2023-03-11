class Solution:
    def minStickers(self, stickers, target: str) -> int:
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c, 0)
        
        dp = {}
        def dfs(t, stick):
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            rem = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    rem += c
            if rem:
                used = float("inf")
                for s in stickCount:
                    if rem[0] in s:
                        used = min(used, dfs(rem, s.copy()))
                    
                dp[rem] = used
                res += used
            return res 
        
        res = dfs(target, {})
        return -1 if res == float("inf") else res
