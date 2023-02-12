class Solution:
    def maxLength(self, arr) -> int:
        def bt(i, prev):
            if i == len(arr):
                return len(prev)
            
            res = bt(i+1, prev)
            
            overlap = False
            j = 0
            s = arr[i]
            while j < len(s):
                if s[j] in prev:
                    overlap = True
                    k = 0
                    while k < j:
                        prev.remove(s[k])
                        k += 1
                    break
                prev.add(s[j])
                j += 1
            res2 = 0
            if not overlap:
                res2 = bt(i+1, prev)
                for c in s:
                    prev.remove(c)
            return max(res2, res)
        
        return bt(0, set())
            
                
            