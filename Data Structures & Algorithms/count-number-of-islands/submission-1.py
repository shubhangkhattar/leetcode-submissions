import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))

            q.append((r,c))

            while q:
                row,col = q.popleft()
                directions = [[-1,0],[+1,0],[0,-1],[0,+1]]
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(m) and c in range(n) and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))



        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    islands += 1

        return islands









            
# CHECK BFS SOLUTION