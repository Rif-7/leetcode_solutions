class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                break
        
        res = []
        i = (l + r) // 2
        l, r = i, i + 1
        for j in range(k):
            lDiff = abs(x - arr[l]) if l >= 0 else float("inf")
            rDiff = abs(x - arr[r]) if r < len(arr) else float("inf")
            
            if lDiff <= rDiff:
                res.append(arr[l])
                l -= 1
            else: 
                res.append(arr[r])
                r += 1
        res.sort()
        return res
        
        
        