class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def bfs(i,j):
            q = deque([(i,j)])
            area = 1
            grid[i][j] = 0
            while q:
                i,j = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j 
                    if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                        continue
                    q.append((r,c))
                    grid[r][c] = 0
                    area += 1

            return area
            
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    max_area = max(max_area,area)
        
        return max_area
                
                