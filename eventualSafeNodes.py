class Solution:
    def eventualSafeNodes(self, graph):
        safe = set()
        visit = set()

        for i in range(len(graph)):
            if not graph[i]:
                safe.add(i)
                visit.add(i)    

        def check(i):
            if i in safe:
                return True
            if i in visit:
                return False
            visit.add(i)
            for n in graph[i]:
                if not check(n):
                    return False
            safe.add(i)
            return True

        for i in range(len(graph)):
            check(i)
        return sorted(list(safe))