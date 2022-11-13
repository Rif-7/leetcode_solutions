class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        
        def find(i, j):
            count = 0
            while 0 <= i and j < N and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
                
            return count
        
        for i in range(len(s)):
            count += find(i, i)
            count += find(i, i+1)

            
        return count
            