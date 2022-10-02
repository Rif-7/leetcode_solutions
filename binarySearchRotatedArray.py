class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        p = 0
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] > nums[mid - 1]:
                r = mid - 1
            else:
                p = mid
                break
        
        if nums[p] <= target <= nums[-1]:
            l = p
            r = len(nums) - 1
        else:
            l = 0
            r = p - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r =  m - 1
            else:
                return m
        return -1 