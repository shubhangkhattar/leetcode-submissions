class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def bfs(i,j):
            q = deque([(i,j)])
            area = 0
            while q:
                i,j = q.popleft()
                print(grid[i][j])
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area += 1
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j 
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        q.append((r,c))
            return area
            
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    max_area = max(max_area,area)
        
        return max_area
                
                