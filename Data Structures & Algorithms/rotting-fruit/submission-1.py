class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = collections.deque()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        def rot_neighbor(r,c):
            
            for dr,dc in directions:
                i = r + dr
                j = c + dc

                if( i < 0 or
                    j < 0 or
                    i >= ROWS or 
                    j >= COLS or
                    grid[i][j] == 0 or
                    grid[i][j] == 2
                ):
                    continue
                
                grid[i][j] = 2
                q.append((i,j))

        
        time = -1
        while q:
            time += 1
            count_rotten = len(q)
            for rotten_fruit in range(count_rotten):
                r,c = q.popleft()
                rot_neighbor(r,c)
        

        for row in grid:
            if 1 in row:
                return -1

        return max(time, 0)



            