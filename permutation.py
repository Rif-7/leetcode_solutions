class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums.copy()]
    
        res = []
        for i in range(len(nums)):
            val = nums.pop(0)
            perms = self.permute(nums)
            
            for p in perms:
                p.append(val)
                
            nums.append(val)
            res.extend(perms)
        return res
            
                        

            
            