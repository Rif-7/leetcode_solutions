class Solution:
    def numSubseq(self, nums, target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)
        i, j = 0, len(nums) - 1
        while i < j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j:
                res += (2**(j - i))
                res %= mod
            i += 1
        
        return res