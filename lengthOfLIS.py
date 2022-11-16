class Solution:
    def lengthOfLIS(self, nums) -> int:
        LIS = [1] * len(nums)
        max_ = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    max_ = max(max_, LIS[i])
                    
        return max_