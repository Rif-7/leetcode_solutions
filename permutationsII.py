import collections

class Solution:
    def permuteUnique(self, nums):
        counter = collections.Counter(nums)
        res = []
        
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in counter:
                if not counter[n]:
                    continue
                counter[n] -= 1
                perm.append(n)
                backtrack(perm)
                perm.pop()
                counter[n] += 1
        backtrack([])
        return res
                