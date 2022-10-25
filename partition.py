class Solution:
    def partition(self, s: str):
        res = []
        partition = []
        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    partition.append(s[i: j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res
    
    def isPali(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True