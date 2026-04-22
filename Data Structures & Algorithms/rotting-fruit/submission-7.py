class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh_orange = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        time = 0

        while fresh_orange > 0 and q:
            q_len = len(q)
            for _ in range(q_len):
                r,c = q.popleft()
                for dr,dc in directions:
                    i = dr+r
                    j = dc+c
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_orange -= 1
                        q.append((i,j))
            time += 1


        return time if fresh_orange == 0 else -1


                