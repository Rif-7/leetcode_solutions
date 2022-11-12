class MySolution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        max_ = nums[n-1]
        nxt = nums[n-2]
        for i in range(n-3, -1, -1):
            nums[i] += max_
            
            max_ = max(max_, nxt)
            nxt = nums[i]
        return max(nums[0], nums[1])


class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2












