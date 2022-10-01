class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxVal = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                stackInd, stackVal = stack.pop()
                maxVal = max(maxVal, (i - stackInd) * stackVal)
                start = stackInd
            stack.append((start, v))
        for i, v in stack:
            maxVal = max(maxVal, (len(heights) -  i) * v)
        return maxVal