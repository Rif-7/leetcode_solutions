class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        def bt(i, prev):
            if i == len(nums):
                if prev in nums:
                    return False
                return prev
            zero = bt(i+1, prev+"0")
            if zero:
                return zero
            one = bt(i+1, prev+"1")
            if one:
                return one
            return False
            
        return bt(0, "")