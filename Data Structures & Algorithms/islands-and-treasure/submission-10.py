class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        visited = set()
        distance = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            
            q_len = len(q)
            for _ in range(q_len):
                i,j = q.popleft()
                grid[i][j] = min(distance,grid[i][j])
                
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j

                    if r in range(m) and c in range(n) and (r,c) not in visited and grid[r][c] != -1 and grid[r][c] != 0:
                        visited.add((i,j))
                        q.append((r,c))
            distance += 1
        

#         Input: [
#   [2147483647,    -1,         0,  2147483647],
#   [2147483647,2147483647,2147483647,  -1],
#   [2147483647,    -1,    2147483647,  -1],
#   [.   0,         -1 ,   2147483647,2147483647]
# ]




