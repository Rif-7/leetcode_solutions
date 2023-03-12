class Solution:
    def maximalSquare(self, matrix) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = {}
        res = 0
        def dfs(i, j): 
            nonlocal res
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= M or j >= N:
                return 0
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)
            diag = dfs(i+1, j+1)

            dp[(i, j)] = 0 
            if matrix[i][j] == "1":
                dp[(i, j)] = 1 + min(down, right, diag)
            res = max(res, dp[(i, j)])
            return dp[(i, j)]
        dfs(0, 0)
        return res * res