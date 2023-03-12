class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        dp = {}
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= R or j >= C or obstacleGrid[i][j] == 1:
                return 0
            
            if i == R-1 and j == C-1:
                return 1
            
            res = dfs(i, j+1)
            res += dfs(i+1, j)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)

