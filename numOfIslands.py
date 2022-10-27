from collections import deque
class MySolution:
    def numIslands(self, grid) -> int:
        visited = set()
        r, c = len(grid), len(grid[0])
        def mark(i, j):
            if not (0 <= i < r) or not (0 <= j < c) or grid[i][j] == "0" or (i, j) in visited:
                return
            
            visited.add((i, j))
            mark(i+1, j)
            mark(i-1, j)
            mark(i, j+1)
            mark(i, j-1)

        res = 0
        
        for i in range(r):
            for j in range(c):
                if (grid[i][j] == "1") and ((i, j) not in visited):
                        res += 1         
                        mark(i, j)
        return res 



class SolutionBFS:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
           
            while q:
                row,col = q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                        q.append((r , c ))
                        visited.add((r, c ))

        for r in range(rows):
            for c in range(cols):
               
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands +=1 

        return islands