class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def bfs(i,j):
            q = deque([(i,j)])
            while q:
                i,j = q.popleft()
                grid[i][j] = 0
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j 
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        q.append((r,c))
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i,j)
        
        return count
                
                