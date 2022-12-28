from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        output = []
        q = deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

class MySolution:
    def maxSlidingWindow(self, nums, k: int):
        minH = []
        for i in range(k):
            heapq.heappush(minH, [-nums[i], i])
        
        res = [-minH[0][0]]
        i, j = 1, k
        while k < len(nums):
            heapq.heappush(minH, [-nums[k], k])
            
            while minH[0][1] < i:
                heapq.heappop(minH)
            
            res.append(-minH[0][0])

            k += 1
            i += 1
        return res