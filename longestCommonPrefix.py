class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]
        for s in strs:
            prefix = self.getPrefix(prefix, s)
        return prefix
            
        
    def getPrefix(self, s1, s2):
        i, j = 0, 0
        prefix = ""
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                break
            prefix += s1[i]
            i += 1
            j += 1
        return prefix