class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])


        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        minHeap = [(-1,0,0)]
        visit = set()
        while minHeap:
            pre_max,i,j = heapq.heappop(minHeap)
            
            if i == m - 1 and j == n - 1 :
                return max(pre_max,grid[i][j])

            visit.add((i,j))
            for dr,dc in directions:
                r = i + dr
                c = j + dc

                if 0 <= r < m and 0 <= c < n and (r,c) not in visit:
                    heapq.heappush(minHeap,(max(pre_max,grid[i][j]),r,c))


        
        return grid[m-1][n-1]



