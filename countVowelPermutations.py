class Solution:
    def countVowelPermutation(self, n: int):
        adj = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        dp = {}

        def dfs(prev, l):
            if l == n:
                return 1
            if (prev, l) in dp:
                return dp[(prev, l)]
            res = 0
            for c in adj[prev]:
                res += dfs(c, l+1)
            dp[(prev, l)] = res
            return res

        res = 0
        for c in ["a", "e", "i", "o", "u"]:
            res += dfs(c, 1)
        return res % (10**9 + 7)


class Solution:
    Memo = {}

    def countVowelPermutation(self, n, c='') -> int:
        if (c, n) in self.Memo:
            return self.Memo[(c, n)]
        if n == 1:
            if c == 'a':
                return 1
            if c == 'e':
                return 2
            if c == 'i':
                return 4
            if c == 'o':
                return 2
            if c == 'u':
                return 1
            if c == '':
                return 5
        else:
            if c == 'a':
                self.Memo[('a', n)] = self.countVowelPermutation(n - 1, 'e')
                return self.Memo[('a', n)]
            if c == 'e':
                self.Memo[('e', n)] = self.countVowelPermutation(
                    n - 1, 'a') + self.countVowelPermutation(n - 1, 'i')
                return self.Memo[('e', n)]
            if c == 'i':
                self.Memo[('i', n)] = self.countVowelPermutation(n - 1, 'a') + self.countVowelPermutation(
                    n - 1, 'e') + self.countVowelPermutation(n - 1, 'o') + self.countVowelPermutation(n - 1, 'u')
                return self.Memo[('i', n)]
            if c == 'o':
                self.Memo[('o', n)] = self.countVowelPermutation(
                    n - 1, 'i') + self.countVowelPermutation(n - 1, 'u')
                return self.Memo[('o', n)]
            if c == 'u':
                self.Memo[('u', n)] = self.countVowelPermutation(n - 1, 'a')
                return self.Memo[('u', n)]
            if c == '':
                Tot = 0
                for i in ['a', 'e', 'i', 'o', 'u']:
                    Tot = Tot + self.countVowelPermutation(n - 1, i)
                return Tot % 1000000007
