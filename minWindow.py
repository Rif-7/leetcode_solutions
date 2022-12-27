class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        checkD, countD = {}, {}
        
        for c in t:
            countD[c] = countD.get(c, 0) + 1
        
        have, need = 0, len(countD)
        i = 0
        res, resLen = [-1, -1], float("Infinity")
        for j in range(len(s)):
            c = s[j]
            checkD[c] = checkD.get(c, 0) + 1
            if c in countD and checkD[c] == countD[c]:
                have += 1
            
            while have == need:
                if (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]
                
                checkD[s[i]] -= 1
                if s[i] in countD and checkD[s[i]] < countD[s[i]]:
                    have -= 1
                i += 1
            
        l, r = res
        return s[l: r + 1] if resLen != float("Infinity") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        res = [0, float("inf")]
        sMap = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] in tMap:
                sMap[s[j]] = sMap.get(s[j], 0) + 1
            
            while self.isSame(tMap, sMap):
                if (j - i + 1) < res[1] - res[0]:
                    res = [i, j+1]
                if s[i] in sMap:
                    sMap[s[i]] -= 1
                    if not sMap[s[i]]:
                        del sMap[s[i]]
                i += 1             
                
                
            j += 1
        return s[res[0]: res[1]] if res[1] != float("inf") else ""
    
    def isSame(self, d1, d2):
        for k, v in d1.items():
            if k not in d2:
                return False
            if v > d2[k]:
                return False
        return True