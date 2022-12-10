class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res