class MySolution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        def helper(n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            
            res = helper(n // 2)
            return res * res * x if n % 2 else res * res
        
        ans = helper(abs(n))
        return ans if n >= 0 else 1 / ans