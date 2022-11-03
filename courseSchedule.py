from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for c in preMap[crs]:
                if not dfs(c): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
            
                