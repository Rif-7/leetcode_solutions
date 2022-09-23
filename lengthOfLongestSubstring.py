class MySolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 1
        i = 0
        j = 1
        prev = {s[0]: 1}
        while j < len(s):
            if prev.get(s[j]) and prev[s[j]] - 1 >= i:
                longest = max(j - i, longest)
                i = prev[s[j]]
                
            prev[s[j]] = j + 1
            j += 1
        
        return max(longest, j-i)

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength