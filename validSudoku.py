from collections import defaultdict
class MySolution:
    def isValidSudoku(self, board) -> bool:
        row = {}
        col = {}
        box = defaultdict(set)
 
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if row.get(board[i][j]):
                        return False
                    row[board[i][j]] = 1
 
                    if board[i][j] in box[(i // 3, j // 3)]:
                        return False
                    box[(i // 3, j // 3)].add(board[i][j])
 
 
                if board[j][i] != ".":
                    if col.get(board[j][i]):
                        return False
                    col[board[j][i]] = 1
 
            row = {}
            col = {}
 
        return True

class Solution:
    def isValidSudoku(self, board) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True