class MySolution:
    def partitionLabels(self, s: str):
        indices = {}
        for i, c in enumerate(s):
            indices[c] = i
            
        preRes = [ indices[s[0]] ]
        for i in range(1, len(s)):
            if i < preRes[-1] and indices[s[i]] > preRes[-1]:
                preRes[-1] = indices[s[i]]
            
            elif indices[s[i]] > preRes[-1]:
                preRes.append(indices[s[i]])
        res = []
        res.append(preRes[0] + 1)
        for i in range(1, len(preRes)):
            res.append(preRes[i] - preRes[i-1])
            
        return res

class Solution:
    def partitionLabels(self, s: str):
        indices = {}
        for i, c in enumerate(s):
            indices[c] = i
            
        preRes = [ indices[s[0]] ]
        for i in range(1, len(s)):
            if i < preRes[-1] and indices[s[i]] > preRes[-1]:
                preRes[-1] = indices[s[i]]
            
            elif indices[s[i]] > preRes[-1]:
                preRes.append(indices[s[i]])
        res = []
        res.append(preRes[0] + 1)
        for i in range(1, len(preRes)):
            res.append(preRes[i] - preRes[i-1])
            
        return res