from collections import deque

class Solution:
    def shortestBridge(self, grid) -> int:
        island1 = set()
        island2 = set()
        N = len(grid)

        
        def mark(i, j, island):
            if not (0 <= i < N) or not (0 <= j < N) or grid[i][j] == 0 or (i, j) in island:
                return
            island.add((i, j))
            mark(i+1, j, island)
            mark(i-1, j, island)
            mark(i, j+1, island)
            mark(i, j-1, island)
        
        shouldBreak = False
        for i in range(N):
            if shouldBreak: break
            for j in range(N):
                if grid[i][j] == 1:
                    mark(i, j, island1)
                    shouldBreak = True
                    break

        shouldBreak = False
        for i in range(N):
            if shouldBreak: break
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in island1:
                    mark(i, j, island2)
                    shouldBreak = True
                    break
        
        q = deque(island1)
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        turns = 0
        visit = set()
        while q:
            l = len(q)
            for k in range(l):
                i, j = q.popleft()
                for dr, dc in dirs:
                    r, c = i+dr, j+dc
                    if (0 <= r < N) and (0 <= c < N) and (r, c) not in visit:
                        if (r, c) in island2:
                            return turns 
                        else:
                            q.append((r, c))
                        visit.add((r, c))
            turns += 1
            

        return -1
    
Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])