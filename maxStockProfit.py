class MySolution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                profit = max(prices[j] - prices[i], profit)
                j += 1
        
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res