class MySolution:
    def countBits(self, n: int):
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            curr = 0
            j = i
            while j:
                curr += j % 2
                j = j // 2
            res[i] = curr
        return res
        
class Solution:
    def countBits(self, n: int):
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp