class Solution:
    def canJump(self, nums) -> bool:
        maxIndex = nums[0]
        for i, n in enumerate(nums):
            if maxIndex < i:
                return False
            maxIndex = max(maxIndex, i + n)
        
        return True