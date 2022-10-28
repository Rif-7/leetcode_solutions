class MySolution:
    def maxAreaOfIsland(self, grid) -> int:
        r, c  = len(grid), len(grid[0])
        used = set()
        def mark(i, j, ):
            if ((i, j) in used 
                or not i in range(r) 
                or not j in range(c) 
                or grid[i][j] == 0
               ):
                return
            
            used.add((i, j))
            mark(i+1, j),
            mark(i-1, j),
            mark(i, j+1),
            mark(i, j-1)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    before = len(used)
                    mark(i, j)
                    after = len(used)
                    res = max(res, after-before)
        return res

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
















