class Solution:
    def combinationSum2(self, cand, target: int):
        cand.sort()
        res = []
        subset = []
        def dfs(i, total):
            if target == total:
                res.append(subset.copy())
                return
            if i >= len(cand) or target < total:
                return
            
            
            subset.append(cand[i])
            dfs(i+1, total+cand[i])
            
            subset.pop()
            while i+1 < len(cand) and cand[i] == cand[i+1]:
                i += 1
            dfs(i+1, total)
        dfs(0, 0)
        return res

s = Solution()
print(s.combinationSum2(
[2,5,2,1,2],
5))