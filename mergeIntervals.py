class Solution:
    def merge(self, intervals):
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                res.append(intervals[i])
            else:
                new = [min(intervals[i][0], res[-1][0]),
                       max(intervals[i][1], res[-1][1])]
                res[-1] = new
        return res