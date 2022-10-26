class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for i in range(n)]
        
        col = set()
        negD = set() # r - c = constant
        posD = set() # r + c = constant
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            
            for c in range(n):
                           
                if c in col or (r - c) in negD or (r + c) in posD:
                    continue
                
                col.add(c)
                negD.add(r-c)
                posD.add(r+c)
                board[r][c] = "Q"
                
                dfs(r + 1)
                
                col.remove(c)
                negD.remove(r-c)
                posD.remove(r+c)
                board[r][c] = "."
        dfs(0)
        return res
                
                
                