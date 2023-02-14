class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        if len(words) <= 1:
            return True
        
        def compare(s1, s2): 
            i = 0
            while i < min(len(s1), len(s2)):
                ind1, ind2 = order.index(s1[i]), order.index(s2[i])
                if ind1 < ind2:
                    return True
                elif ind1 > ind2:
                    return False
                i += 1
                
            return len(s1) <= len(s2)
        i, j = 0, 1
        while j < len(words):
            if not compare(words[i], words[j]):
                return False
            i, j = i + 1, j + 1
        return True
        
        
        
    