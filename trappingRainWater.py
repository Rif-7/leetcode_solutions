from socket import RDS_CANCEL_SENT_TO
from turtle import right
from xml.dom import HierarchyRequestErr


class MySolution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            if height[l] < height[l + 1]:
                l += 1
            elif height[r] < height[r - 1]:
                r -= 1
            elif height[l] <= height[r]:
                k = l + 1
                while height[l] > height[k] and k < r:
                    ans += height[l] - height[k]
                    k += 1
                l = k
            elif height[r] < height[l]:
                k = r - 1
                while height[r] > height[k] and l < k:
                    ans += height[r] - height[k]
                    k -= 1
                r = k
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        res = 0
        while l < r:
            if (leftMax <= rightMax):
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]