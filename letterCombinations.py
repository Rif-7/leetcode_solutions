class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
            
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i):
            if i == len(digits) - 1:
                return list(letterMap[digits[i]])
            res = []
            combs = dfs(i+1)
            for x in letterMap[digits[i]]:
                curr = [x+y for y in combs]
                res.extend(curr)
            return res
        return dfs(0)
        