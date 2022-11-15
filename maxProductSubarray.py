class Solution:
    def maxProduct(self, nums) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        
        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin *n, n)
            res = max(res, currMax)
        
        return res