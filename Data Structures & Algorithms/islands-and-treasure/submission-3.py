class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        visit = set()

        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def add(i,j):
            
            value = grid[i][j] + 1
            
            for dr,dc in directions:

                r = i + dr
                c = j + dc
                
                if (r < 0 or 
                    c < 0 or 
                    r >= ROWS or 
                    c >= COLS or 
                    (r,c) in visit or 
                    grid[r][c] == -1):
                    continue
                grid[r][c] = value
                visit.add((r,c))
                q.append((r,c))
            

        while q:
            r,c = q.popleft()
            add(r,c)

