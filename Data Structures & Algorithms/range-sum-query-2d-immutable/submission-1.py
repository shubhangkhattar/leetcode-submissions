class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        m = len(matrix)
        n = len(matrix[0])

        self.sumMatrix = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                self.sumMatrix[i][j] = matrix[i][j]
                if i > 0:
                    self.sumMatrix[i][j] += self.sumMatrix[i-1][j]
                if j > 0:
                    self.sumMatrix[i][j] += self.sumMatrix[i][j-1]
                if i > 0 and j > 0:
                    self.sumMatrix[i][j] -= self.sumMatrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        res += self.sumMatrix[row2][col2]

        if row1 > 0:
            res -= self.sumMatrix[row1-1][col2]
        if col1 > 0:
            res -= self.sumMatrix[row2][col1-1]
        if row1 > 0 and col1 >0:
            res += self.sumMatrix[row1-1][col1-1]

        return res




[3, 0, 1, 4, 2], 
[5, 6, 3, 2, 1], 
[1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], 
[1, 0, 3, 0, 5]

[[3, 3, 4, 8, 10], 
[8, 14, 18, 24, 27], 
[9, 17, 21, 28, 36], 
[13, 22, 26, 34, 49], 
[14, 23, 30, 38, 58]]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)