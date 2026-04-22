class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def dfs(i,j,prev,path):
            
            if i in range(m) and j in range(n) and matrix[i][j] > prev and (i,j) not in path: 
                path.add((i,j))
                ans = max(
                    dfs(i+1,j,matrix[i][j],path),
                    dfs(i,j+1,matrix[i][j],path),
                    dfs(i-1,j,matrix[i][j],path),
                    dfs(i,j-1,matrix[i][j],path),
                )
                path.remove((i,j))
                return ans
            else:
                return len(path)
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result,dfs(i,j,-1,set()))
        
        return result

            
            