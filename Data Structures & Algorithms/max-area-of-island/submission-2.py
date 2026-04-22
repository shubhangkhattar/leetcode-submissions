class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        max_area = 0
        
        def bfs(i,j):
            visited = set()
            area = 0
            q = deque()
            q.append((i,j))
            while q:
                q_n = len(q)
                for _ in range(q_n):
                    i,j = q.popleft()
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i,j) not in visited:
                        area += 1
                        visited.add((i,j))
                        q.append((i+1,j))
                        q.append((i-1,j))
                        q.append((i,j+1))
                        q.append((i,j-1))
            return area

        
        for i in range(m):
            for j in range(n):
                max_area = max(max_area,bfs(i,j))

        return max_area
                