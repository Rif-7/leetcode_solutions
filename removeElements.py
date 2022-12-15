class Solution:
    def removeElement(self, nums, val: int) -> int:

        i = 0
        while i < len(nums) and nums[i] != val:
            i += 1
        free = i
        
        for j in range(i+1, len(nums)):
            if nums[j] != val:
                nums[free] = nums[j]
                free += 1
        return free