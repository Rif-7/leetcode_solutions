class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        largest = ""
        
        def find(i, j):
            curr = s[i]
            
            j += 1
            
            while j < N and s[j] == s[i]:
                j += 1
            
            i -= 1
            while i >= 0 and j < N and s[i] == s[j]:
                i -= 1
                j += 1
            
            return [s[i+1:j], j]
        
        for i in range(len(s)):
            pal = find(i, i)
            if len(pal[0]) > len(largest):
                largest = pal[0]
                
            i = pal[1]
        return largest