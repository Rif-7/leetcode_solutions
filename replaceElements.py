class Solution:
    def replaceElements(self, arr):
        right = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if right > arr[i+1]:
                temp = right
                right = arr[i]
                arr[i] = temp
            else:
                right = arr[i]
                arr[i] = arr[i+1]
        return arr