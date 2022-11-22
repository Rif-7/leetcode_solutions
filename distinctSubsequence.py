class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dic = {}
        def dfs(prev, i, k):
            if prev == t:
                return 1
            if (i == len(s) or k == len(t) or
               len(prev) + (len(s) - i + 1) < len(t)):
                return 0
            if (i, prev) in dic:
                return dic[(i, prev)]
            
            dic[(i, prev)] = dfs(prev, i+1, k)
            if s[i] == t[k]:
                dic[(i, prev)] += dfs(prev + s[i], i+1, k+1)
            
            return dic[(i, prev)]
        return dfs("", 0, 0)