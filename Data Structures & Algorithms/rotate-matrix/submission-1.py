class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(m):
            matrix[i] = reversed(matrix[i])
        
