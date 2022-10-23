import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            self.addToMax(num)
            return 
        
        l1, l2 = len(self.maxHeap), len(self.minHeap)
        if l1 > l2:
            if num >= -self.maxHeap[0]:
                self.addToMin(num)
            else:
                val = heapq.heappop(self.maxHeap)
                self.addToMin(-val)
                self.addToMax(num)
        else:
            if num <= self.minHeap[0]:
                self.addToMax(num)
            else:
                val = heapq.heappop(self.minHeap)
                self.addToMax(val)
                self.addToMin(num)
                
                

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0]
    
    def addToMax(self, val):
        heapq.heappush(self.maxHeap, -val)
    
    def addToMin(self, val):
        heapq.heappush(self.minHeap, val)
        
