class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        ROWS = [False] * m
        COLS = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ROWS[i] = True
                    COLS[j] = True

        for i in range(m):
            for j in range(n):
                if ROWS[i] == True or COLS[j] == True:
                    matrix[i][j] = 0

        