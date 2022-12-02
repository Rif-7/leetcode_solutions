class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                res += 1
                prev = min(intervals[i][1], prev)
            else:
                prev = intervals[i][1]
                    
        return res