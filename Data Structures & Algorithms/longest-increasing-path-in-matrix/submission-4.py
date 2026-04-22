class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        memo = {}

        def dfs(i,j,prev):

            if (i,j,prev) in memo:
                return memo[(i,j,prev)]
            
            memo[(i,j,prev)] = 0

            if i in range(m) and j in range(n) and matrix[i][j] > prev:
                
                max_result = max(
                    dfs(i-1,j,matrix[i][j]),
                    dfs(i,j-1,matrix[i][j]),
                    dfs(i+1,j,matrix[i][j]),
                    dfs(i,j+1,matrix[i][j]),
                )

                memo[(i,j,prev)] = max_result + 1

            return  memo[(i,j,prev)]

        result = 0 

        for i in range(m):
            for j in range(n):
                result = max(dfs(i,j,-1),result)

        return result
