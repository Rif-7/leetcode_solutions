import heapq

class SeatManager:

    def __init__(self, n: int):
        self.minHeap = [1 + i for i in range(n)]
        heapq.heapify(self.minHeap)

    def reserve(self) -> int:
        return heapq.heappop(self.minHeap)

    def unreserve(self, seatNumber: int) -> None:
        return heapq.heappush(self.minHeap, seatNumber)    
    

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)