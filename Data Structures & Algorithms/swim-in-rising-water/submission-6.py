class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        min_heap = [(grid[0][0],0,0)]
        
        directions = [(1,0),(0,1),(0,-1),(-1,0)]

        visited = set()

        while min_heap:
            time,i,j = heapq.heappop(min_heap)
            visited.add((i,j))
            if i == m-1 and j == n-1:
                return time
            
            for dr,dc in directions:
                
                r = dr + i
                c = dc + j

                if r in range(m) and c in range(n) and (r,c) not in visited:
                    heapq.heappush(min_heap,(max(time,grid[r][c]),r,c))

                
                



            