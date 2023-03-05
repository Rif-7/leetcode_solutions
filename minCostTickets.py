class Solution:
    def mincostTickets(self, days, costs) -> int:
        dp = {}
        def dfs(i, freePass):
            if i >= len(days):
                return 0
            if days[i] < freePass:
                return dfs(i+1, freePass)
            if i in dp:
                return dp[i]

            # purchase a 1 day ticket on i'th day
            one = dfs(i+1, days[i] + 1) + costs[0]
            # purchase a 7 day ticket on i'th day
            seven = dfs(i+1, days[i] + 7) + costs[1]
            # purchase a 30 day ticket on i'th day
            thirty = dfs(i+1, days[i] + 30) + costs[2]
            dp[i] = min(one, seven, thirty)
            return dp[i]
        return dfs(0, -1)