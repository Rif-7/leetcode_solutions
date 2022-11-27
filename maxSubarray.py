class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            if total <= 0:
                total = 0
            total += n
            res = max(total, res)
        return res
        
        
        
        