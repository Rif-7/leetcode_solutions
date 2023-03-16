class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        l, r = 0,  len(cardPoints) - k
        total = sum(cardPoints[r:])

        res = total
        while r < len(cardPoints):
            total = total - cardPoints[r] + cardPoints[l]
            res = max(res, total)
            l += 1
            r += 1
        return res
