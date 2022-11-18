class Solution:
    def canPartition(self, nums) -> bool:
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        subSums = set()
        subSums.add(0)
        target = sum_ // 2
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in subSums:
                if t + nums[i] == target:
                    return True
                nextDP.add(t)
                nextDP.add(t + nums[i])
            subSums = nextDP
        return False
        
        
            