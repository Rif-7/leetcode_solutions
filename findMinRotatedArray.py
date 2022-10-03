class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[0] <= nums[m]:
                l = m + 1
            elif nums[m - 1] <= nums[m]:
                r = m - 1
            else:
                p = m
                break
        return nums[p]
                