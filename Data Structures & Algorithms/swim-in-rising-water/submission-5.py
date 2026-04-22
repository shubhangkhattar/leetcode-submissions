class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        minHeap = [(grid[0][0],0,0)]
        visited = set()

        time = 0

        while minHeap:
            pre_max,i,j = heapq.heappop(minHeap)

            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == m-1 and j == n-1:
                break

            for dr,dc in directions:
                r = i + dc
                c = j + dr

                if 0 <= r < m and 0 <= c < n and (r,c) not in visited:
                    heapq.heappush(minHeap,(max(grid[r][c],pre_max),r,c))


        return pre_max



            
