class MySolution:
    def exist(self, board, word: str) -> bool:
        r, c = len(board), len(board[0])
        def search(i, j, k, used):
            if used.get((i, j), 0):
                return False
            if k >= len(word):
                return True
            
            used[(i, j)] = True
            if j+1 < c and board[i][j+1] == word[k]:
                if search(i, j+1, k+1, used):
                    return True
            if j-1 > -1 and board[i][j-1] == word[k]:
                if search(i, j-1, k+1, used):
                    return True
            if i+1 < r and board[i+1][j] == word[k]:
                if search(i+1, j, k+1, used):
                    return True
            if i-1 > -1 and board[i-1][j] == word[k]:
                if search(i-1, j, k+1, used):
                    return True
            del used[(i, j)]
            return False
        
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j] and search(i, j, 1, {}):
                    return True
        return False