class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        path = []

        def dfs(i,j,prevVal):
            
            if 0 <= i < m and 0 <= j < n and matrix[i][j] > prevVal:
   
                return 1 + max(dfs(i-1,j,matrix[i][j]),
                 dfs(i,j-1,matrix[i][j]), 
                 dfs(i+1,j,matrix[i][j]), 
                 dfs(i,j+1,matrix[i][j]))

            return 0

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result,dfs(i,j,-1))

        return result