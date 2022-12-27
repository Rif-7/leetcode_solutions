class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res  = []
        i = 0
        
        while i < len(nums):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                l, r = j + 1, len(nums) - 1
                while l < r:
                    c, d = nums[l], nums[r]

                    if a + b + c + d < target:
                        l += 1
                    elif a + b + c + d > target:
                        r -= 1
                    else:
                        if [a, b, c, d] not in res:
                            res.append([a, b, c, d])
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
            i += 1
            
        return res
            