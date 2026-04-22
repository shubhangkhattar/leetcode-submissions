class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        
        
        pacific_side = set()
        atlantic_side = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(i,j,prev,side):
            if heights[i][j] >= prev:
                side.add((i,j))
            else:
                return
            for dr,dc in directions:
                r = dr + i
                c = dc + j

                if r in range(m) and c in range(n) and (r,c) not in side:
                    dfs(r,c,heights[i][j],side)

        result = []

        for i in range(m):
            dfs(i,0,0,pacific_side)
            dfs(i,n-1,0,atlantic_side)

        for j in range(n):
            dfs(0,j,0,pacific_side)
            dfs(m-1,j,0,atlantic_side)
        
        result = []


        return list(pacific_side.intersection(atlantic_side))
