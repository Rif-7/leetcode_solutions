from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()
        res = []
        added = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                if crs not in added:
                    res.append(crs)
                    added.add(crs)
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visiting.remove(crs)
            preMap[crs] = []
            if crs not in added:
                res.append(crs)
                added.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                res = []
                break
        return res
            
            