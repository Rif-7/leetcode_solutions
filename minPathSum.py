class Solution:
    def minPathSum(self, grid) -> int:
        M, N = len(grid), len(grid[0])
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i >= M or j >= N:
                return float("inf")
            
            if i == M-1 and j == N-1:
                return grid[i][j]
            
            res = min(dfs(i+1, j), dfs(i, j+1))
            dp[(i, j)] = res + grid[i][j]
            return dp[(i, j)]
        
        return dfs(0, 0)
