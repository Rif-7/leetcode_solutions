class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        marked = set()
        
        def mark(i, j):
            if (
                not (0 <= i < r) or not (0 <= j < c) 
                or (i, j) in marked
                or board[i][j] == "X"
            ):
                return
            
            marked.add((i, j))
            
            mark(i, j+1)
            mark(i, j-1)
            mark(i+1, j)
            mark(i-1, j)
            
        
        for i in range(r):
            mark(i, 0)
            mark(i, c-1)
        
        for i in range(c):
            mark(0, i)
            mark(r-1, i)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i, j) not in marked:
                    board[i][j] = "X"
        
        
        
        