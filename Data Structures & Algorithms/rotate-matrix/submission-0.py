class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        ans = []

        for j in range(n):
            col = []
            for i in range(m):
                col.insert(0,matrix[i][j])
            ans.append(col)

        for i in range(m):
            for j in range(n):
                matrix[i][j] = ans[i][j]