class Solution:
    def maxProfit(self, prices) -> int:
        curr = 0
        res = 0
        currMax = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[curr]:
                if currMax >= prices[i] - prices[curr]:
                    res += currMax
                    currMax = 0
                    curr = i
                else:
                    currMax = max(currMax, prices[i] - prices[curr])
            else:
                res += currMax
                currMax = 0
                curr = i
        res += currMax
        return res