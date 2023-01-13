class Solution:
    def searchRange(self, nums, target: int):
        
        def search(l, r):
            left, right = float("inf"), float("-inf")
            res = [left, right]
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1 
                else:
                    left = search(l, m-1)[0]
                    res[0] = min(left, m)
                    right = search(m+1, r)[1]
                    res[1] = max(right, m)
                    break
            
            return res
        
        res = search(0, len(nums) - 1)
        if res[0] == float("inf"):
            return [-1, -1]
        return res
            