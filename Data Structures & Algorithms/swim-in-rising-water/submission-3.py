class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        minHeap = [(grid[0][0],0,0)]
        visit = set()
        while minHeap:
            pre_max,r,c = heapq.heappop(minHeap)
            
            if r == m-1 and c == n-1:
                return pre_max

            visit.add((r,c))
            for dr,dc in directions:
                i = dr + r
                j = dc + c
                if 0 <= i < m and 0 <= j < n and (i,j) not in visit:
                    heapq.heappush(minHeap,(max(pre_max,grid[i][j]),i,j))
        

            
            
