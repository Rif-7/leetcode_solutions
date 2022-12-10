from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = []

    def add(self, point) -> None:
        self.counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(px - x) == abs(py - y)) and (x != px or y != py):
                res += self.counts[(px, y)] * self.counts[(x, py)]
        return res
