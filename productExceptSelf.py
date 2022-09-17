class MySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        l = len(nums)
        answer = [1] * l
        # return the product of all the values after the current index
        # prev is the product of all values before the current index
        def solve(index, prev):
            if index == l - 1:
                answer[index] = prev
                return nums[index]
            
            res = solve(index + 1, prev * nums[index])
            answer[index] = prev * res
            return res * nums[index]
        solve(0, 1)
        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res