class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        r = len(matrix)
        c = len(matrix[0])
        self.dp = [[0]*(c+1) for i in range(r+1)]

        for i in range(r):
            row_sum = 0
            for j in range(c):
                row_sum += matrix[i][j]
                self.dp[i+1][j+1] = self.dp[i][j+1] + row_sum
        
        print(self.dp)
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# [3, 0, 1, 4, 2], 
# [5, 6, 3, 2, 1], 
# [1, 2, 0, 1, 5], 
# [4, 1, 0, 1, 7], 
# [1, 0, 3, 0, 5],
#  0.   1.  2.  3.   4

# [0, 0, 0, 0, 0, 0], 
# [0, 3, 3, 4, 8, 10], 
# [0, 8, 14, 18, 24, 27], 
# [0, 9, 17, 21, 28, 36], 
# [0, 13, 22, 26, 34, 49], 
# [0, 14, 23, 30, 38, 58]

# (row2 + 1, col2 + 1) - (row1 + 1, col2) - (row1, col2+1) + (row1, col1) 

34 - 13 - 8 + 3

[2, 1, 4, 3]



