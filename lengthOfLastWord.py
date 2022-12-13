class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currLen = 0
        j = 0
        while j < len(s):
            if s[j] != " ":
                currLen += 1
                j += 1
            else:
                while s[j] == " ":
                    j += 1
                    if j == len(s):
                        return currLen
                currLen = 0
            
        return currLen
            