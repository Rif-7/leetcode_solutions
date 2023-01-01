class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        res = 1
        i, j = 0, 0
        total = 0
    
        while j < len(nums):
            while i < j and total + k + nums[j] < (nums[j] * (j - i + 1)):
                total -= nums[i]
                i += 1
            res = max(res, (j - i + 1))
            total += nums[j]
            j += 1
        return res
            