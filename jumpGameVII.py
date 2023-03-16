from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            lBound = max(farthest + 1, i + minJump)
            uBound = min(i + maxJump + 1, len(s))
            for j in range(lBound, uBound):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        return False
