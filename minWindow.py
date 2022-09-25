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




class MySolution: 
    def minWindow(s: str, t: str) -> str:
            res = ""
            tDict = {}
            for c in t:
                tDict[c] = tDict.get(c, 0) + 1
            
            
            i = 0
            while not tDict.get(s[i]):
                i += 1
                
            sDict = {}
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                
                if j != i and s[j] == s[i] and tDict[s[i]] == sDict[s[i]]:
                        if sDict[s[j]] == 1:
                            del sDict[s[j]]
                        else:
                            sDict[s[j]] -= 1
                        i += 1
                        while not tDict.get(s[i]):
                            i += 1
                        curr = s[i:j+1]
                        
                if tDict.get(s[j]) and tDict[s[j]] > sDict.get(s[j], 0):
                    sDict[s[j]] = sDict.get(s[j], 0) + 1
                    
                    if sDict == tDict:
                        if len(curr) < len(res) or not len(res):
                            res = curr
                        if sDict[s[i]] == 1:
                            del sDict[s[i]]
                        else:
                            sDict[s[i]] -= 1
                        i += 1 if i < j else 0
                        while i < j and not tDict.get(s[i]):
                            i += 1
                        curr = s[i: j+1]
            return res


