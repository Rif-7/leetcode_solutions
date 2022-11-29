class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        record = [False, False, False]
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                record[0] = True
            if t[1] == target[1]:
                record[1] = True
            if t[2] == target[2]:
                record[2] = True
            
            if all(record):
                return True
        
        return False
            
        
        
        
        
        