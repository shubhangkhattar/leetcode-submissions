class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = set()

        directions = [(1,0),(0,1),(0,-1),(-1,0)]

        def bfs(i,j):
            nonlocal visited
            q = deque()
            q.append((i,j))
            while q:
                q_n = len(q)

                for _ in range(q_n):
                    r,c = q.popleft()
                    visited.add((r,c))
                    for dr,dc in directions:

                        nr, nc = r + dr, c + dc

                        if (0 <= nr < m and
                            0 <= nc < n and 
                            grid[nr][nc] == "1" and 
                            (nr,nc) not in visited):
                            q.append((nr,nc))
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    result += 1
                    bfs(i,j)
        
        return result
                