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

        print(fresh_orange)

        if fresh_orange == 0:
            return 0
        

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        time = -1

        while q:
            time += 1
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

        print(fresh_orange)


        return -1 if time == 0 or fresh_orange != 0 else time


                