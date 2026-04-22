class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.mark_the_island(i,j,m,n,grid)
                    islands += 1

        return islands

    def mark_the_island(self,i,j,m,n,matrix):
        if 0 <= i < m and 0 <= j < n and matrix[i][j] == "1":
            matrix[i][j] = -1
            self.mark_the_island(i+1,j,m,n,matrix)
            self.mark_the_island(i-1,j,m,n,matrix)
            self.mark_the_island(i,j+1,m,n,matrix)
            self.mark_the_island(i,j-1,m,n,matrix)
            
