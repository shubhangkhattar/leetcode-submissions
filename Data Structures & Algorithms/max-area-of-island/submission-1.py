class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        max_area = 0
        
        def dfs(i,j):
            nonlocal visited
            if 0 <= i < m and 0 <= j < n and (i,j) not in visited and grid[i][j] == 1:
                visited.add((i,j))
                return (1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1))
            return 0
        
        for i in range(m):
            for j in range(n):
                max_area = max(max_area,dfs(i,j))

        return max_area
                