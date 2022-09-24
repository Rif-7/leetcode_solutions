class MySolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dct = {}
        for c in s1:
            dct[c] = dct.get(c, 0) + 1
            
        i = 0
        dct2 = {}
        for j, c in enumerate(s2):
            dct2[c] = dct2.get(c, 0) + 1
            if not dct.get(c):
                i = j + 1
                dct2 = {}
            elif dct2[c] > dct[c]:
                dct2[c] -= 1
                while s2[i] != c:
                    if dct2[s2[i]] > 1:
                        dct2[s2[i]] -= 1
                    else:
                        del dct2[s2[i]]
                        
                    i += 1
                i += 1
            if dct2 == dct:
                return True
        return False



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
















