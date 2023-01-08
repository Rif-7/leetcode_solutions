class Solution:
    def find132pattern(self, nums) -> bool:
        stack = []
        currMin = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            while stack and stack[-1][0] <= n:
                stack.pop()
                
            if stack and stack[-1][1] < n:
                return True
            stack.append((n, currMin))
            currMin = min(currMin, n)
            