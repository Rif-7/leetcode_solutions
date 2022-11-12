class MySolution:
    def climbStairs(self, n: int) -> int:
        res = [-1] * (n+1)
        def dfs(k):
            if k > n:
                return 0
            elif k == n:
                return 1
            
            if res[k] != -1:
                return res[k]
            
            curr = dfs(k+1) + dfs(k+2)
            res[k] = curr
            return curr

        return dfs(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
        
        
        

