class Solution:
    def minimumTotal(self, triangle) -> int:
        N = len(triangle)
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= N:
                return 0
            if j > i:
                return float("inf")

            one = triangle[i][j] + dfs(i+1, j)
            two = triangle[i][j] + dfs(i+1, j+1)
            
            dp[(i, j)] = min(one, two)
            return dp[(i, j)]

        return dfs(0, 0)