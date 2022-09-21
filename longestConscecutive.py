class SortedSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prev = {}
        nums = sorted(nums)
        for i in nums:
            if prev.get(i):
                continue
            val = prev.get(i-1, 0) + 1
            prev[i] = val
            
        ans = 0
        for a in prev.values():
            if a > ans:
                ans = a
        return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for i in numSet:
            if (i - 1) not in numSet:
                l = 1
                while (i + l) in numSet:
                    l += 1
                if l > longest:
                    longest = l
        return longest