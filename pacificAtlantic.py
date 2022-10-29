class Solution:
    def pacificAtlantic(self, heights):
        r, c = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(i, j, visit, prev):
            if (
                (i, j) in visit 
                or i < 0 or i == r or j < 0 or j == c 
                or heights[i][j] < prev
            ):
                return
            
            visit.add((i, j))
            dfs(i, j+1, visit,heights[i][j])
            dfs(i, j-1, visit, heights[i][j])
            dfs(i+1, j, visit, heights[i][j])
            dfs(i-1, j, visit, heights[i][j])

        for i in range(c):
            dfs(0, i, pac, heights[0][i])
            dfs(r-1, i, atl, heights[r-1][i])
        for i in range(r):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, c-1, atl, heights[i][c-1])
        
        return atl & pac
            
        
            
            