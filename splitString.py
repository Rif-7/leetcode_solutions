class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, prev):
            if i == len(s) and prev != int(s):
                return True
            j = i
            while j < len(s):
                num = int(s[i:j+1])
                if prev == None:
                    if num != 0 and backtrack(j+1, num):
                        
                        return True
                elif (prev - num) == 1:
                    if backtrack(j+1, num):
                        return True
                elif num > prev:
                    return False
                j += 1
            return False
        return backtrack(0, None)