class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):
            nonlocal visited
            if (0 <= i < m and 
                0 <= j < n and 
                grid[i][j] == "1" and
                (i,j) not in visited
                ):
                visited.add((i,j))
                for dr,dc in directions:
                    row = dr + i
                    col = dc + j
                    dfs(row,col)
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    result += 1
                    dfs(i,j)
        
        return result
                