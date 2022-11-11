class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k+1):
            tempPrices = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if tempPrices[d] > prices[s] + p:
                    tempPrices[d] = prices[s] + p
                    
            prices = tempPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1
        