class Solution:
    def maximumRemovals(self, s: str, p: str, removable) -> int:
        def isSubSeq(k):
            rmvble = set()
            for i in range(k+1):
                rmvble.add(removable[i])
            
            j = 0
            for i in range(len(s)):
                if i in rmvble:
                    continue
                if s[i] == p[j]:
                    j += 1
                    if j == len(p):
                        return True
            return False
        
        res = -1
        l, r = 0, len(removable) - 1
        while l <= r:
            m = (l + r) // 2
            if isSubSeq(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res + 1
    
        