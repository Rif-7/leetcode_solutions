class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        si, ei = 0, 0
        count, res = 0, 0
        while si < len(start):
            if start[si] < end[ei]:
                count += 1
                si += 1
            else:
                count -= 1
                ei += 1
            res = max(count, res)

        return res
        