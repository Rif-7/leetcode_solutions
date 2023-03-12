from functools import cache


class Solution:
    def maxAlternatingSum(self, nums) -> int:
        n = len(nums)

        @cache
        def dfs(i, p):
            if i >= len(nums):
                return 0
            num = nums[i] if p else -nums[i]
            choose = dfs(i+1, not p) + num
            notChoose = dfs(i+1, p)
            return max(choose, notChoose)
        return dfs(0, True)
