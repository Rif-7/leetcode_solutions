class MySolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        answer = []
        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1
        nums = list(freqMap.keys())
        count = list(freqMap.values())
        
        for k in range(k):
            largest = - 1
            index = None
            for i, n in enumerate(count):
                if n > largest:
                    largest = n
                    index = i
            answer.append(nums[index])
            count[index] = -1
        return answer


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res