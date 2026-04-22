class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        m = len(grid)
        n = len(grid[0])

        area = 0

        def dfs(i,j):
            nonlocal area
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                area += 1
                grid[i][j] = 0
                dir = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in dir:
                    row = i + dr
                    col = j + dc
                    dfs(row,col)
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0 
                    dfs(i,j)
                    max_area = max(area,max_area)
        
        return max_area
