class Solution:
    def maxSumMinProduct(self, nums) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        
        res = 0
        stack = []
        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                ind, val = stack.pop()
                total = prefix[i] - prefix[ind]
                res = max(res, total * val)
                newStart = ind
            stack.append((newStart, n))
        
        for ind, val in stack:
            total = prefix[-1] - prefix[ind]
            res = max(res, total * val)
        return res % (10**9 + 7)