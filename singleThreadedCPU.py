import heapq

class Solution:
    def getOrder(self, tasks):
        tasks = [[e, i, p] for i, [e, p] in enumerate(tasks)]
        heapq.heapify(tasks)
        currTask = None
        res = []
        avail = []
        time = 1
        while tasks:
            while tasks and tasks[0][0] == time:
                # time, index, processing time
                t, i, p = heapq.heappop(tasks)
                heapq.heappush(avail, [p, i])
            
            
            if not currTask or currTask <= time:
                if avail:
                    p, i = heapq.heappop(avail)
                    res.append(i)
                    currTask = time + p
                else:
                    currTask = None
                
            if currTask and tasks and currTask <= tasks[0][0]:
                time = currTask
            elif currTask and tasks and currTask > tasks[0][0]:
                time = tasks[0][0]
            elif not currTask and tasks:
                time = tasks[0][0]
                
            
        
        while avail:
            res.append(heapq.heappop(avail)[1])
        return res
                        
        
        