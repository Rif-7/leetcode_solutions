class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        res = 1
        currLen1 = 1
        currLen2 = 1
        for i in range(len(arr) - 2, -1, -1):
            if i % 2:
                if arr[i] > arr[i+1]:
                    currLen1 += 1
                    currLen2 = 1
                elif arr[i] < arr[i+1]:
                    currLen1 = 1
                    currLen2 += 1
                else:
                    currLen1 = currLen2 = 1
            else:
                if arr[i] < arr[i+1]:
                    currLen1 += 1
                    currLen2 = 1
                elif arr[i] > arr[i+1]:
                    currLen1 = 1
                    currLen2 += 1
                else:
                    currLen1 = currLen2 = 1
            res = max(res, currLen1, currLen2)
        return res
