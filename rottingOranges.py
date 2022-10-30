from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        r, c = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()
        
        def mark(i, j):
            nonlocal fresh
            if i not in range(r) or j not in range(c) or grid[i][j] in (0, 2):
                return
            
            grid[i][j] = 2
            q.append((i, j))
            fresh -= 1
            
            
        def rot(i, j):
            mark(i+1, j), 
            mark(i-1, j),
            mark(i, j-1),
            mark(i, j+1)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            l = len(q)
            for k in range(l):
                i, j = q.popleft()
                rot(i, j)
            time += 1
                
        return -1 if fresh else time 