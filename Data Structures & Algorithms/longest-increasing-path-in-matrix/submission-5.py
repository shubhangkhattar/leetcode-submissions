class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        memo = {}

        def dfs(i,j,prev):

            if i in range(m) and j in range(n) and matrix[i][j] > prev:
                
                if (i,j) in memo:
                    return memo[(i,j)]
                
                memo[(i,j)] = max(
                    dfs(i+1,j,matrix[i][j]),
                    dfs(i-1,j,matrix[i][j]),
                    dfs(i,j+1,matrix[i][j]),
                    dfs(i,j-1,matrix[i][j]),
                ) + 1
                return memo[(i,j)]

            return 0

        maxResult = 0

        for i in range(m):
            for j in range(n):
                maxResult = max(maxResult,dfs(i,j,-1))

        return maxResult
