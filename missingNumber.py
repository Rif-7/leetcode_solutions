class Solution:
    def missingNumber(self, nums) -> int:
        s = 0
        for n in nums:
            s += n
        
        return (((len(nums) + 1) * (len(nums))) // 2) - s