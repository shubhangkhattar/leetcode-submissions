from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])
        
        INF = 2147483647
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(i,j):
            distance = 0
            visited = set()
            
            q = deque()
            q.append((i,j))
            distance = 0
            while q:
                q_len = len(q)
                for i in range(q_len):
                    i,j = q.popleft()
                    visited.add((i,j))
                    grid[i][j] = min(grid[i][j], distance)
                    for dr,dc in directions:
                        r = i + dr
                        c = j + dc
                        if (0 <= r < m and 
                            0 <= c < n and
                            (r,c) not in visited and 
                            grid[r][c] != -1 and grid[r][c] != 0
                            ):
                            q.append((r,c))
                distance += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i,j)
            
                
                


