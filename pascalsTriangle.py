class Solution:
    def generate(self, numRows: int):
        res = [[1]]
        for i in range(numRows - 1):
            curr = []
            curr.append(res[0][0])
            
            for j in range(0, len(res[-1]) - 1):
                curr.append(res[-1][j] + res[-1][j+1])
            
            curr.append(res[-1][-1])
            res.append(curr)
            
        return res